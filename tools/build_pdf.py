from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "whole_root_lab_digital_materia_medica_v0_1.pdf"


DISCLAIMER = (
    "Educational use only. Not medical advice. No diagnosis, treatment, or dosing "
    "recommendations. Consult qualified professionals for clinical decisions."
)


HERBS = [
    {
        "name": "Birch",
        "latin": "Betula pendula / Betula pubescens / Betula spp.",
        "family": "Betulaceae",
        "part": "Leaf is the regulatory herbal substance; bark is important in phytochemical research.",
        "relevance": "Betula pubescens is documented in Icelandic flora as Birki, and Betula pendula / Betula pubescens are central birch species in northern Europe.",
        "ratings": "Traditional use; In vitro / preclinical; Regulatory monograph",
        "sections": [
            (
                "Traditional Context",
                [
                    "Birch belongs naturally in a Nordic materia medica because birches are boreal and north-temperate trees. Rastogi, Pandey, and Rawat describe Betula species as trees and shrubs of temperate and boreal climate zones in the northern hemisphere, with long-standing use of bark and bark extracts in traditional medicine. The same review reports that documented traditional uses most often cluster around bone and joint complaints, renal uses, sap, and some cosmetic uses. In a student text, that history should be read as ethnobotanical context rather than proof of clinical efficacy.",
                    "For the Icelandic angle, the Flora of Iceland entry documents Betula pubescens as downy birch, with Icelandic names including Birki. That makes birch a strong first plant for WholeRootLab because it has local recognition, a northern ecological identity, and a scientific literature base broad enough for careful study.",
                ],
            ),
            (
                "Constituents",
                [
                    "The Betula review reports several major constituent groups across the genus: triterpenoids, diarylheptanoids, phenylbutanoids, lignans, phenolics, and flavonoids. Betulin and betulinic acid are especially important bark-associated compounds in the research literature, while the EMA/HMPC birch leaf materials focus on Betula pendula and/or Betula pubescens leaf preparations.",
                    "For students, the key distinction is part-specific evidence. Birch leaf, birch bark, sap, pollen, and purified bark triterpenes are not interchangeable. A responsible monograph should name the plant part every time a research or safety statement is made.",
                ],
            ),
            (
                "Evidence Snapshot",
                [
                    "The strongest v0.1 claim is that birch has a substantial preclinical and review literature, not that it has proven broad clinical benefits. Rastogi et al. summarize in vitro and in vivo findings for immunomodulatory, anti-inflammatory, antimicrobial, antiviral, antioxidant, antidiabetic, dermatological, gastroprotective, hepatoprotective, antiarthritic, and anticancer research areas. That is a map of research activity, not a license to market birch as a treatment.",
                    "The EMA/HMPC summary for Betulae folium is useful because it narrows the practical herbal-medicine frame to birch leaf, specifically Betula pendula and/or Betula pubescens leaf. EMA states that EU herbal monographs evaluate safety and efficacy data, including long-standing use, and provide safety information for herbal medicinal products. For student study, this is a good example of how regulatory monographs can be more conservative than broad phytochemical reviews.",
                    "Source quality note: use Rastogi et al. as the broad genus-level research map, EMA/HMPC as the conservative leaf-specific regulatory anchor, and Flora of Iceland as the local identity anchor. If a future WholeRootLab entry adds birch sap, birch pollen, or birch bark, it should become a separate sub-entry or clearly marked section rather than being folded into the birch leaf profile.",
                ],
            ),
            (
                "Safety Notes",
                [
                    "The EMA public summary states that reported side effects with birch leaf medicines include diarrhoea, nausea/vomiting, itching, rash, and stuffy or runny nose, with unknown frequency. It also states that birch leaf medicines must not be used by people hypersensitive to birch leaf or birch pollen, or by patients with conditions where reduced fluid intake is recommended, such as severe heart or kidney disease.",
                    "Student caution: birch pollen allergy is common enough that natural does not mean low-risk. Also avoid translating bark-triterpene or purified-compound research into leaf-infusion assumptions.",
                ],
            ),
            (
                "Student Study Notes",
                [
                    "Key takeaway: Birch is an excellent training herb for learning part-specific evidence. Learn the difference between Betula leaf monographs, bark phytochemistry, sap traditions, and purified compounds such as betulin.",
                    "Terms to learn: triterpenoids, betulin, betulinic acid, flavonoids, regulatory monograph, preclinical evidence.",
                    "What to verify next: Which Betula species grow locally, which plant part is being studied, and whether a claim comes from traditional use, cell/animal work, human research, or an official monograph.",
                    "Next expansion: create separate database fields for plant part, preparation type, and evidence level before adding more birch material. Birch is especially prone to category drift because students may encounter leaf teas, sap traditions, bark extracts, pollen allergy, and purified triterpene research under the same common name. A clean WholeRootLab entry should force the reader to ask, which birch material is this source actually about?",
                ],
            ),
        ],
        "references": [
            "Rastogi S, Pandey MM, Kumar Singh Rawat A. Medicinal plants of the genus Betula - traditional uses and a phytochemical-pharmacological review. Journal of Ethnopharmacology. 2015;159:62-83. doi: 10.1016/j.jep.2014.11.010. PMID: 25449458. PMCID: PMC7126499. https://pmc.ncbi.nlm.nih.gov/articles/PMC7126499/",
            "European Medicines Agency. Betulae folium - herbal medicinal product. Reference Number: EMA/482160/2015. https://www.ema.europa.eu/en/medicines/herbal/betulae-folium",
            "Flora of Iceland. Betula pubescens, Downy Birch, Birki. https://www.iceland-nh.net/plants/data/Betula-pubescens/betula_pubescens.html",
        ],
    },
    {
        "name": "Meadowsweet",
        "latin": "Filipendula ulmaria (L.) Maxim.",
        "family": "Rosaceae",
        "part": "Flowering tops and flowers.",
        "relevance": "Flora of Iceland documents Filipendula ulmaria as Mjadjurt, growing on moist ground.",
        "ratings": "Traditional use; In vitro / preclinical; Regulatory monograph",
        "sections": [
            (
                "Traditional Context",
                [
                    "Meadowsweet is a classic European herb of wet meadows, damp woodland edges, and river margins. The Flora of Iceland page documents it as Mjadjurt and describes it growing on moist ground, which fits its wider European ecological profile. EMA/HMPC identifies the herbal substances as Filipendula ulmaria herb and flowers, and its assessment report reviews traditional use under the EU traditional herbal medicinal product framework.",
                    "Traditional references often connect meadowsweet with discomfort, feverish states, urinary/digestive elimination, and rheumatic contexts. In this MVP, those statements should remain in the traditional-context section unless they are tied to a specific regulatory or experimental source. This keeps the student-facing tone careful and avoids turning heritage into a treatment claim.",
                ],
            ),
            (
                "Constituents",
                [
                    "EMA/HMPC reports salicylates among the main volatile-oil components, especially salicylaldehyde, with salicylates mostly present as glycosides and assumed to be less than 0.5 percent. EMA also lists flavonoids, including spiraeoside and other quercetin and kaempferol derivatives, hydrolysable tannins such as rugosin D, plus trace coumarin, mucilage, carbohydrates, and ascorbic acid.",
                    "Olennikov, Kashchenko, and Chirikova studied teas from four Filipendula species and found methyl salicylate and salicylaldehyde dominance in essential oil samples. Their work also highlighted phenolic compounds, polysaccharides, antioxidant activity in assay systems, and anti-complement activity of water-soluble polysaccharide fractions. For students, meadowsweet is a good case study in how taste, volatile compounds, tannins, and salicylate chemistry intersect.",
                ],
            ),
            (
                "Evidence Snapshot",
                [
                    "The evidence base is strongest for phytochemistry, regulatory traditional-use assessment, and laboratory mechanisms. Olennikov et al. analyzed meadowsweet tea preparations for nutrients, phytochemicals, and bioactivities, including antioxidant assays, alpha-amylase and alpha-glucosidase inhibition, advanced glycation end-product inhibition, and anti-complement activity. These are functional and laboratory findings, not proof of clinical outcomes.",
                    "Van der Auwera et al. investigated Filipendula ulmaria constituents and metabolites in an in vitro gastrointestinal biotransformation model. They reported that glycosylated flavonoids decreased in the colon compartment while aglycones such as quercetin, apigenin, naringenin, and kaempferol increased; genuine and metabolized extracts showed stronger COX-1 than COX-2 inhibition. Their conclusion was that anti-inflammatory activity may be explained by additive or synergistic effects of original constituents and metabolites.",
                    "For a student, the important lesson is evidence translation. Meadowsweet has plausible phytochemical and in vitro anti-inflammatory mechanisms, but the monograph should not present that as clinical proof.",
                    "Source quality note: EMA/HMPC is the anchor for traditional-use framing and salicylate caution; Olennikov et al. is best used for beverage chemistry and assay-level bioactivity; Van der Auwera et al. is best used for mechanism and metabolism. None of these sources should be rewritten as a student dosing guide or as proof that meadowsweet treats inflammatory disease in humans.",
                ],
            ),
            (
                "Safety Notes",
                [
                    "The key safety caution is salicylate sensitivity. EMA/HMPC states that because salicylates are present, Filipendula ulmaria should not be used in cases of hypersensitivity to salicylates. For a student product, it is also prudent to flag professional supervision for people using anticoagulants, antiplatelet medicines, NSAIDs, or aspirin, and for pregnancy/lactation, because salicylate-related assumptions can be clinically relevant even when the herb is not equivalent to aspirin.",
                    "Student caution: do not reduce meadowsweet to natural aspirin. That phrase is tempting but misleading. The plant contains multiple constituent groups, salicylates are present largely as glycosides, and human clinical meaning depends on preparation, dose, metabolism, and person-specific risk.",
                ],
            ),
            (
                "Student Study Notes",
                [
                    "Key takeaway: Meadowsweet is a strong teaching herb for separating phytochemical plausibility from clinical claims.",
                    "Terms to learn: salicylates, salicylaldehyde, methyl salicylate, flavonoid glycosides, aglycones, tannins, COX-1, COX-2, NF-kB.",
                    "What to verify next: the exact plant part, whether the source is an EMA monograph or an in vitro paper, and whether any student summary accidentally overstates anti-inflammatory evidence.",
                    "Next expansion: add a comparison table that separates traditional indications, phytochemical markers, laboratory mechanisms, and human-evidence gaps. Meadowsweet is a useful teaching herb precisely because the story sounds simple at first, then becomes more nuanced when salicylates, tannins, flavonoids, gut metabolism, and regulatory wording are placed side by side.",
                ],
            ),
        ],
        "references": [
            "European Medicines Agency, Committee on Herbal Medicinal Products. Assessment report on Filipendula ulmaria (L.) Maxim., herba and Filipendula ulmaria (L.) Maxim., flos. EMA/HMPC/434892/2010. 12 July 2011. https://www.ema.europa.eu/en/documents/herbal-report/final-assessment-report-filipendula-ulmaria-l-maxim-herba-and-filipendula-ulmaria-l-maxim-flos-first-version_en.pdf",
            "Olennikov DN, Kashchenko NI, Chirikova NK. Meadowsweet teas as new functional beverages: comparative analysis of nutrients, phytochemicals and biological effects of four Filipendula species. Molecules. 2016;22(1):16. doi: 10.3390/molecules22010016. PMID: 28035976. PMCID: PMC6155584. https://pmc.ncbi.nlm.nih.gov/articles/PMC6155584/",
            "Van der Auwera A, Peeters L, Foubert K, Piazza S, Vanden Berghe W, Hermans N, Pieters L. In vitro biotransformation and anti-inflammatory activity of constituents and metabolites of Filipendula ulmaria. Pharmaceutics. 2023;15(4):1291. doi: 10.3390/pharmaceutics15041291. PMID: 37111776. PMCID: PMC10146082. https://pmc.ncbi.nlm.nih.gov/articles/PMC10146082/",
            "Flora of Iceland. Filipendula ulmaria, Meadowsweet, Mjadjurt. https://www.iceland-nh.net/plants/data/Filipendula-ulmaria/filipendula_ulmaria.html",
        ],
    },
    {
        "name": "Stinging Nettle",
        "latin": "Urtica dioica L.",
        "family": "Urticaceae",
        "part": "Leaf/herb for this student entry; root evidence should be tracked separately.",
        "relevance": "Flora of Iceland documents Urtica dioica as Brenninetla, noting it is introduced and mostly found near human settlements.",
        "ratings": "Traditional use; In vitro / preclinical; Human evidence; Regulatory monograph",
        "sections": [
            (
                "Traditional Context",
                [
                    "Stinging nettle is a foundational European herbal study plant, but the Icelandic context needs nuance. The Flora of Iceland page states that Urtica dioica is not a natural element of Icelandic flora and is mainly found near human settlements; the Icelandic name is Brenninetla. That makes nettle relevant to an Icelandic materia medica as a present and recognizable plant, but not as a pristine native-symbol plant.",
                    "Taheri et al. describe Urtica dioica as a Urticaceae plant found in many countries and used medicinally since at least ancient Greek times. Devkota et al. also describe a long history of use as food and traditional medicine. Traditional uses vary widely by region and plant part, which is exactly why this entry should teach students to separate leaf/herb, root, seed, food use, and topical urtication.",
                ],
            ),
            (
                "Constituents",
                [
                    "Taheri et al. report a broad range of phytochemicals in Urtica dioica, including phenolic compounds, sterols, fatty acids, alkaloids, terpenoids, flavonoids, and lignans. Devkota et al. focus on nutritional and food-functional aspects and describe leaves as rich in bioactive compounds, including flavonoids, phenolic acids, amino acids, carotenoids, and fatty acids.",
                    "For students, nettle is useful because it sits between food, herb, and phytochemical study. Its leaves are discussed as nutritional material and as herbal material, but that does not make every therapeutic claim equally supported.",
                ],
            ),
            (
                "Evidence Snapshot",
                [
                    "The v0.1 evidence message should be conservative: nettle has extensive review literature and many preclinical findings, plus some human-study areas, but the strength of evidence depends heavily on plant part and indication. Taheri et al. summarize reported pharmacological activities across antiviral, antimicrobial, antioxidant, anti-inflammatory, antiarthritis, antidiabetic, and other areas, while explicitly framing the review as guidance for future work to estimate clinical value. Devkota et al. emphasize nutritional composition, bioactive constituents, reported food-functional activities, and the need for formulation, stability, and clinical studies.",
                    "The EMA/HMPC Urticae folium page confirms that nettle leaf has an EU herbal monograph, with Urtica dioica L. and Urtica urens L. as botanical sources for nettle leaf. EMA describes herbal monographs as documents that evaluate available information, including non-clinical, clinical, and long-standing-use data, and provide safety information. This makes EMA useful for teaching the difference between regulatory traditional-use framing and broad scientific review claims.",
                    "Source quality note: Taheri et al. is a broad pharmacology review, Devkota et al. is stronger for nutritional and food-functional framing, EMA/HMPC is the regulatory anchor for nettle leaf, and Flora of Iceland clarifies the local ecological status. A good student entry should not merge leaf, herb, root, seed, and food claims into one general nettle does X statement.",
                ],
            ),
            (
                "Safety Notes",
                [
                    "Fresh nettle stings because of hairs that can irritate skin; Devkota et al. describe the plant as covered with stinging hairs that release mediators such as histamine and acetylcholine. Student handling notes should include gloves and careful identification.",
                    "Because nettle may be used as food, tea, supplement, root extract, or topical plant material, safety depends on form and context. For this student MVP, avoid pregnancy/lactation use without professional guidance, avoid assuming leaf evidence applies to root preparations, and flag professional advice for people with kidney disease, fluid-balance restrictions, diabetes medicines, blood pressure medicines, anticoagulants, or complex medication plans. These cautions are intentionally conservative for an educational sample.",
                ],
            ),
            (
                "Student Study Notes",
                [
                    "Key takeaway: Nettle is a bridge plant. Study it as food, leaf/herb medicine, root research, and ecology separately.",
                    "Terms to learn: phenolic acids, flavonoids, carotenoids, amino acids, urtication, dioecious, regulatory monograph, food-functional activity.",
                    "What to verify next: plant part, preparation type, whether the evidence is nutritional, traditional, preclinical, or human, and whether the Icelandic source describes it as native or introduced.",
                ],
            ),
        ],
        "references": [
            "Taheri Y, Quispe C, Herrera-Bravo J, Sharifi-Rad J, Ezzat SM, Merghany RM, Shaheen S, Azmi L, Mishra AP, Sener B, Kilic M, Sen S, Acharya K, Nasiri A, Cruz-Martins N, Tsouh Fokou PV, Ydyrys A, Bassygarayev Z, Dastan SD, Alshehri MM, Calina D, Cho WC. Urtica dioica-derived phytochemicals for pharmacological and therapeutic applications. Evidence-Based Complementary and Alternative Medicine. 2022;2022:4024331. doi: 10.1155/2022/4024331. PMID: 35251206. PMCID: PMC8894011. https://pmc.ncbi.nlm.nih.gov/articles/PMC8894011/",
            "Devkota HP, Paudel KR, Khanal S, Baral A, Panth N, Adhikari-Devkota A, Jha NK, Das N, Singh SK, Chellappan DK, Dua K, Hansbro PM. Stinging nettle (Urtica dioica L.): nutritional composition, bioactive compounds, and food functional properties. Molecules. 2022;27(16):5219. doi: 10.3390/molecules27165219. PMID: 36014458. PMCID: PMC9413031. https://pmc.ncbi.nlm.nih.gov/articles/PMC9413031/",
            "European Medicines Agency. Urticae folium - herbal medicinal product. https://www.ema.europa.eu/en/medicines/herbal/urticae-folium",
            "Flora of Iceland. Urtica dioica, Common Nettle, Brenninetla. https://www.iceland-nh.net/plants/data/Urtica-dioica/urtica_dioica.html",
        ],
    },
]


def make_styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=30,
            leading=34,
            textColor=colors.HexColor("#1f3a32"),
            alignment=TA_CENTER,
            spaceAfter=16,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=12,
            leading=17,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#4c5f59"),
            spaceAfter=22,
        ),
        "h1": ParagraphStyle(
            "H1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=24,
            textColor=colors.HexColor("#1f3a32"),
            spaceBefore=12,
            spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=16,
            textColor=colors.HexColor("#3d5a4f"),
            spaceBefore=10,
            spaceAfter=5,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.6,
            leading=13.4,
            textColor=colors.HexColor("#202422"),
            alignment=TA_LEFT,
            spaceAfter=6,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8,
            leading=10.2,
            textColor=colors.HexColor("#303835"),
            spaceAfter=4,
        ),
        "label": ParagraphStyle(
            "Label",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#203d34"),
        ),
        "footer": ParagraphStyle(
            "Footer",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=7,
            leading=8,
            textColor=colors.HexColor("#6b7570"),
            alignment=TA_CENTER,
        ),
    }


def para(text, style):
    safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return Paragraph(safe, style)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#dfe7e2"))
    canvas.line(0.75 * inch, 0.55 * inch, A4[0] - 0.75 * inch, 0.55 * inch)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(colors.HexColor("#6b7570"))
    canvas.drawCentredString(A4[0] / 2, 0.36 * inch, f"WholeRootLab Digital Materia Medica v0.1 | Page {doc.page}")
    canvas.restoreState()


def identity_table(herb, styles):
    data = [
        [para("Latin name", styles["label"]), para(herb["latin"], styles["small"])],
        [para("Family", styles["label"]), para(herb["family"], styles["small"])],
        [para("Plant part", styles["label"]), para(herb["part"], styles["small"])],
        [para("Nordic/Icelandic relevance", styles["label"]), para(herb["relevance"], styles["small"])],
        [para("Evidence rating", styles["label"]), para(herb["ratings"], styles["small"])],
    ]
    table = Table(data, colWidths=[1.6 * inch, 4.8 * inch], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f3f7f4")),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#c8d8cf")),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#dbe6df")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return table


def build_story(styles):
    story = []
    story.append(Spacer(1, 1.0 * inch))
    story.append(para("WholeRootLab", styles["title"]))
    story.append(para("Digital Materia Medica v0.1", styles["subtitle"]))
    story.append(
        para(
            "A cautious, evidence-first sample for herbal medicine students studying Nordic and Iceland-relevant plants.",
            styles["subtitle"],
        )
    )
    story.append(Spacer(1, 0.25 * inch))
    story.append(para("Disclaimer", styles["h2"]))
    story.append(para(DISCLAIMER, styles["body"]))
    story.append(Spacer(1, 0.2 * inch))
    story.append(para("Evidence Ratings", styles["h2"]))
    for item in [
        "Traditional use - documented historical or ethnobotanical use.",
        "In vitro / preclinical - cell, enzyme, laboratory, or animal evidence.",
        "Human evidence - human observational or clinical research.",
        "Regulatory monograph - EMA/HMPC or comparable official herbal monograph.",
        "Insufficient evidence - plausible or traditional claim that needs stronger confirmation.",
    ]:
        story.append(para(item, styles["body"]))
    story.append(PageBreak())

    for index, herb in enumerate(HERBS, start=1):
        story.append(para(f"{index}. {herb['name']}", styles["h1"]))
        story.append(identity_table(herb, styles))
        story.append(Spacer(1, 0.08 * inch))
        for title, paragraphs in herb["sections"]:
            story.append(para(title, styles["h2"]))
            for paragraph in paragraphs:
                story.append(para(paragraph, styles["body"]))
        story.append(para("References", styles["h2"]))
        for ref in herb["references"]:
            story.append(para(ref, styles["small"]))
        if index != len(HERBS):
            story.append(PageBreak())
    return story


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    styles = make_styles()
    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=0.7 * inch,
        leftMargin=0.7 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.7 * inch,
        title="WholeRootLab Digital Materia Medica v0.1",
        author="WholeRootLab",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=footer)])
    doc.build(build_story(styles))
    print(OUTPUT)


if __name__ == "__main__":
    main()
