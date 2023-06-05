from django.shortcuts import render
from crews.models import Crew, Island, Has
from crews.forms import CrewForm, IslandForm, HasForm

def crews(request):

    all_crews = Crew.objects.all()
    return render(
        request,
        "crews/crews.html",
        {"crews" : all_crews}
    )


def crew(request, crew_id):

    formulaire = HasForm()

    the_crew = Crew.objects.get(crew_id = crew_id)
    has = Has.objects.filter(crew_id = crew_id)
    island_list = []
    for h in has:
        island = Island.objects.get(island_id=h.island.island_id)
        island_list.append({"name": island.island_name,
                                 "pic": island.island_pic,
                                 "id": island.island_id,
                                 "has_id": h.has_id})

    return render(
        request,
        "crews/crew.html",
        {"crew" : the_crew, "island_list" : island_list, "formulaire": formulaire}
    )

def formulaireCreationCrew(request):

    formulaire = CrewForm()

    return render(
        request,
        "crews/formulaireCreationCrew.html",
        {"form": formulaire}
    )

def creerCrew(request):

    form = CrewForm(request.POST, request.FILES)
    if form.is_valid():
        crew_name = form.cleaned_data['crew_name']
        crew_pic = form.cleaned_data['crew_pic']
        crew = Crew()
        crew.crew_name = crew_name
        crew.crew_pic = crew_pic
        crew.save()
    else:
        form = CrewForm()

    return render(
        request,
        "crews/createCrew.html",
        {"crew_name": crew_name, "form" : form}
    )

def ajouterIslandAuCrew(request, crew_id):
    formulaire = HasForm(request.POST)
    if formulaire.is_valid():
        island = formulaire.cleaned_data['island']

        try:
            Has.objects.get(island_id = island.island_id, crew_id = crew_id)
        except Has.DoesNotExist:
            has = Has()
            has.crew = Crew.objects.get(crew_id = crew_id)
            has.island = Island.objects.get(island_id = island.island_id)
            has.save()

    formulaire = HasForm()
    the_crew = Crew.objects.get(crew_id = crew_id)
    has = Has.objects.filter(crew_id = crew_id)
    island_list = []
    for h in has:
        island = Island.objects.get(island_id=h.island.island_id)
        island_list.append({"name": island.island_name,
                                 "pic": island.island_pic,
                                 "id": island.island_id,
                                 "has_id": h.has_id})
    return render(request,
        "crews/crew.html",
        {"crew" : the_crew,
         "island_list" : island_list,
          "formulaire": formulaire}
        )

def supprimerCrew(request, crew_id):

    crew = Crew.objects.get(crew_id = crew_id)
    crew.delete()
    all_crews = Crew.objects.all()
    return render(
        request,
        "crews/crews.html",
        {"crews" : all_crews}
    )

def formulaireModificationCrew(request, crew_id):

    crew = Crew.objects.get(crew_id = crew_id)
    formulaire = CrewForm(instance = crew)
    return render(
        request,
        "crews/formulaireModificationCrew.html",
        {'form': formulaire, 'crew': crew}
    )

def modifierCrew(request, crew_id):
    crew = Crew.objects.get(crew_id = crew_id)
    formulaire = CrewForm(request.POST, request.FILES, instance = crew)
    if formulaire.is_valid():
        formulaire.save()
        crew = Crew.objects.get(crew_id = crew_id)
    return render(
        request,
        "crews/traitementFormulaireModificationCrew.html",
        {'crew': crew}
    )

def supprimerIslandForCrew(request, crew_id, has_id):

    formulaire = HasForm()

    has = Has.objects.filter(has_id = has_id)
    has.delete()

    the_crew = Crew.objects.get(crew_id = crew_id)
    has = Has.objects.filter(crew_id = crew_id)
    island_list = []
    for h in has:
        island = Island.objects.get(island_id=h.island.island_id)
        island_list.append({"name": island.island_name,
                                 "pic": island.island_pic,
                                 "id": island.island_id,
                                 "has_id": h.has_id})

    return render(
        request,
        "crews/crew.html",
        {"crew" : the_crew, "island_list" : island_list, "formulaire": formulaire}
    )


def island(request, island_id):

    print(island_id)
    island = Island.objects.get(island_id = island_id)
    print(island.island_name)
    return render(
        request,
        "crews/island.html",
        {"island" : island}
    )


def islands(request):

    all_islands = Island.objects.all()

    return render(
        request,
        "crews/islands.html",
        {"islands" : all_islands}
    )

def formulaireCreationIsland(request):

    formulaire = IslandForm()

    return render(
        request,
        "crews/formulaireCreationIsland.html",
        {"form": formulaire}
    )

def creerIsland(request):

    form = IslandForm(request.POST, request.FILES)
    if form.is_valid():
        island_name = form.cleaned_data['island_name']
        island_region = form.cleaned_data['island_region']
        island_pic = form.cleaned_data['island_pic']
        island = Island()
        island.island_name = island_name
        island.island_region = island_region
        island.island_pic = island_pic
        island.save()
    else:
        form = IslandForm()

    return render(
        request,
        "crews/createIsland.html",
        {"island_name": island_name, "form" : form}
    )

def supprimerIsland(request, island_id):

    island = Island.objects.get(island_id = island_id)
    island.delete()
    all_islands = Island.objects.all()
    return render(
        request,
        "crews/islands.html",
        {"islands" : all_islands}
    )

def formulaireModificationIsland(request, island_id):

    island = Island.objects.get(island_id = island_id)
    formulaire = IslandForm(instance = island)
    return render(
        request,
        "crews/formulaireModificationIsland.html",
        {'form': formulaire, 'island': island}
    )

def modifierIsland(request, island_id):
    island = Island.objects.get(island_id = island_id)
    formulaire = IslandForm(request.POST, request.FILES, instance = island)
    if formulaire.is_valid():
        formulaire.save()
        island = Island.objects.get(island_id = island_id)
    return render(
        request,
        "crews/traitementFormulaireModificationIsland.html",
        {'island': island}
    )
