import graphene
from graphene_django import DjangoObjectType

from animals.models import Kind, Family


class FamilyType(DjangoObjectType):
    class Meta:
        model = Family
        fields = ('id', 'name', 'kind_set')


class KindType(DjangoObjectType):
    class Meta:
        model = Kind
        fields = ('id', 'name', 'family')


class Query(graphene.ObjectType):
    all_kinds = graphene.List(KindType)
    all_families = graphene.List(FamilyType)
    kinds_by_name = graphene.List(KindType, name=graphene.String(required=True))
    family_by_id = graphene.Field(FamilyType, id=graphene.Int(required=True))

    def resolve_kinds_by_name(self, root, name):
        return Kind.objects.filter(name__contains=name)

    def resolve_all_kinds(self, root):
        return Kind.objects.all()

    def resolve_all_families(self, root):
        return Family.objects.all()

    def resolve_family_by_id(self, root, id):
        return Family.objects.get(id=id)

class FamilyMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)

    # The class attributes define the response of the mutation
    family = graphene.Field(FamilyType)

    @classmethod
    def mutate(cls, root, info, name):
        family = Family.objects.create(name=name)
        # Notice we return an instance of this mutation
        return FamilyMutation(family=family)

"""
Пример запроса
mutation myFirstMutation {
    createFamily(name: "Tiger") {
        family {
            name
        }
        
    }
}
"""
class Mutation(graphene.ObjectType):
    create_family = FamilyMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
