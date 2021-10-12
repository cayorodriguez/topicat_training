import spacy_streamlit
import typer


def main(models: str, default_text: str):
    models = [name.strip() for name in models.split(",")]
    spacy_streamlit.visualize(models, "Quan tenia 14 anys, la seva família el va enviar a treballar al municipi de Sant Martí de Provençals, actualment annexionat a Barcelona, on entrà com aprenent en un comerç de farines. L'amo del negoci el va inscriure a classes nocturnes i el va iniciar als ideals republicans. Amb aquesta base va continuar una formació autodidacta. Els anys següents va estudiar a fons la doctrina de Francesc Pi i Margall i les tesis internacionalistes. El 1883 entrà a treballar com a revisor en la línia de ferrocarril Barcelona-Cervera de la Marenda (Rosselló francès) i ho aprofità per exercir d'enllaç amb Ruiz Zorrilla, del Partit Republicà Progressista, del qual es feu militant. El 1886 va recolzar el pronunciament militar del general Villacampa, partidari de Ruiz Zorrilla, la finalitat del qual era proclamar la República. Després que l'intent fracassés, Ferrer i Guàrdia hagué d'exiliar-se a París, on va ser acompanyat per Teresa Sanmartí (Teresina), amb qui va tenir tres fills.", visualizers=["textcat"])


if __name__ == "__main__":
    try:
        typer.run(main)
    except SystemExit:
        pass
