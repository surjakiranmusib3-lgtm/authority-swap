const fs=require('fs'), path=require('path');
const dir=__dirname;
const rows=JSON.parse(fs.readFileSync(path.join(dir,'p2c-fact-audit-ledger-input.json'),'utf8').replace(/^\uFEFF/,''));
const byId=Object.fromEntries(rows.map(r=>[r.id,r]));
const facts=`
C001|yellowstone.establishment_year=1872
C002|statue_liberty.sculptor=Frederic-Auguste Bartholdi
C003|gutenberg_bible.print_city=Mainz
C004|bell.telephone_patent_year=1876
C005|human_typical_somatic.autosome_pairs=22;human_typical_somatic.sex_chromosome_pairs=1;human_typical_somatic.chromosome_pairs=23
C006|rna.canonical_base_uracil=present;rna.canonical_base_thymine=absent
C007|komodo_dragon.largest_living_lizard=true
C008|red_panda.family=Ailuridae
C009|bell.first_call_recipient=Thomas A. Watson
C010|statue_liberty.island=Liberty Island
C011|yellowstone.area_share_wyoming=96%;yellowstone.area_share_montana=3%;yellowstone.area_share_idaho=1%
C012|statue_liberty.crown_window_count=25
C013|statue_liberty.france_construction_start_year_selected_page=1876;statue_liberty.pedestal_construction_start_year=1884
C014|gutenberg.printing_partner=Johannes Fust
C015|gutenberg_bible.vellum_share=approximately one quarter
C016|bell.telephone_patent_number=174465
C017|rna.backbone_sugar=ribose
C018|transcription.product=RNA copy of a gene DNA sequence
C019|translation.location=ribosomes in the cytoplasm
C020|red_panda.activity_in_human_care=dawn and dusk
C021|yellowstone.establishment_year=1872;yellowstone.army_administration_start_year=1886;yellowstone.nps_takeover_year=1918
C022|yellowstone.first_lake_hotel_built_year=1891;yellowstone.old_faithful_inn_opened_year=1904
C023|statue_liberty.copper_weight_lb=176000;statue_liberty.framework_weight_lb=440000
C024|statue_liberty.base_top_to_torch_height=151 feet 1 inch;statue_liberty.ground_to_pedestal_height=154 feet
C025|red_panda.adult_body_length_inches=22 to 24.6;red_panda.adult_tail_length_inches=14.6 to 18.6
C026|bell.patent_priority_supreme_court_year=1888;telephone.first_transcontinental_call_year=1915
C027|gutenberg_bible.estimated_print_run=180 copies;gutenberg_bible.vellum_share=approximately one quarter
C028|human_typical_somatic.autosome_pairs=22;human_typical_somatic.autosome_count=44
C029|genetic_code.codon_count=64;genetic_code.amino_acid_codon_count=61
C030|komodo_dragon.typical_wild_weight_lb=154;komodo_dragon.largest_verified_weight_lb=366
C031|yosemite.grant_year=1864;yosemite.national_park_designation_year=1890
C032|gutenberg_bible.alternate_line_count_name=42-line Bible
C033|statue_liberty.replacement_torch_installation_year=1986
C034|corps_discovery.trek_start_date=May 14 1804
C035|genetic_code.uag_function=stop signal
C036|red_panda.native_range_himalayas=present
C037|statue_liberty.current_torch_flame_coating=24 karat gold leaf
C038|telephone.first_transcontinental_call_east_endpoint=New York;telephone.first_transcontinental_call_west_endpoint=San Francisco
C039|messenger_rna.function=carries a gene protein information from nucleus to cytoplasm
C040|statue_liberty.dedication_date=October 28 1886
C041|gutenberg_bible.language=Latin
C042|rna.typical_strandedness=single stranded
C043|giant_panda.wild_diet_almost_exclusive=bamboo
C044|hot_springs.national_reservation_year=1832;yellowstone.establishment_year=1872
C045|statue_liberty.original_torch_2018_destination=Statue of Liberty Museum Torch Gallery
C046|phenotype.definition=an individual observable traits
E001|erupted_magma.name=lava
E002|seismic_body_wave.fastest_arrival=P wave
E003|igneous_rock.formation=molten rock solidification
E004|sedimentary_rock.formation=sediment compaction and cementation
E005|challenger_deep.ocean=western Pacific
E006|ocean_thermocline.upper_layer=warmer mixed surface water;ocean_thermocline.lower_layer=cooler deep water
E007|spring_tide.lunar_phases=new and full moon
E008|seawater.average_salinity_ppt=35
E009|coastal_estuary.brackish_water_components=river fresh water and seawater
E010|geyser.periodic_eruption_cause=constrictions in plumbing allow pressure build up
E011|earthquake.magnitude_location_dependence=one source size value per magnitude scale;earthquake.intensity_location_dependence=varies by observation location
E012|seismic_p_wave.traverses_liquid=true;seismic_s_wave.traverses_liquid=false;seismic_p_wave.traverses_solid=true
E013|seawater.most_prevalent_ion_pair=chloride and sodium
E014|thermohaline_circulation.density_drivers=temperature and salinity
E015|great_lakes.small_tide_masking_causes=wind and barometric pressure changes
E016|coastal_upwelling.rising_water_temperature=typically cold;coastal_upwelling.rising_water_nutrients=typically rich
E017|grand_canyon.kaibab_age_ma_2020_table=270;grand_canyon.tapeats_age_ma_2020_table=508
E018|igneous_grain_size.slow_cooling_effect=larger mineral grains
E019|soil.clay_vs_sand_absorption=clay absorbs less water more slowly;soil.low_absorption_effect=greater runoff
E020|magma.high_viscosity_gas_escape=gas escapes less easily;magma.trapped_gas_pressure_effect=pressure can build to explosive release
E021|ocean.average_depth_m=3682;challenger_deep.depth_m=approximately 10935
E022|sound.seawater_speed_m_s=approximately 1500;sound.air_speed_m_s=approximately 340
E023|lunar_day.duration=24 hours 50 minutes;noaa_tide_example.high_tides_per_lunar_day=2
E024|knot.km_per_hour=1.85;noaa_strong_tidal_current.example_speed_knots=8 or more
E025|usgs_simulation.p_wave_arrival_seconds=12.3;usgs_simulation.s_wave_arrival_seconds=24.7;usgs_simulation.rayleigh_arrival_seconds=about 32
E026|usgs_simulation.p_wave_speed_m_s=5400;usgs_simulation.s_wave_speed_m_s=2700
E027|grand_canyon.kaibab_age_ma_2020_table=270;grand_canyon.redwall_age_ma_2020_table=340;grand_canyon.coconino_age_ma_2020_table=280;grand_canyon.tapeats_age_ma_2020_table=508
E028|spring_tide.lunar_phases=new and full moon;spring_tide.occurrences_per_lunar_month=2
E029|global_groundwater.total_volume_cubic_miles=5614000;global_groundwater.fresh_volume_cubic_miles=2526000;global_groundwater.saline_volume_cubic_miles=3088000
E030|colorado_river.grand_canyon_segment_miles=277;colorado_river.total_journey_miles=approximately 1450
E031|groundwater.below_water_table_zone=saturated zone;groundwater.saturated_zone_voids=completely water filled
E032|ocean_sound.travel_distance_drivers=water temperature and pressure
E033|grand_canyon.phantom_granite_age_ma_2020_table=1662;grand_canyon.horn_creek_granite_age_ma_2020_table=1713;grand_canyon.ruby_gabbro_age_ma_2020_table=1716;grand_canyon.elves_chasm_age_ma_2020_table=1840
E034|coal.rock_class=biologic sedimentary rock
E035|great_lakes.freshwater_estuary_exists=true;great_lakes.freshwater_estuary_mixing=differing river and lake freshwater characteristics
E036|earth.water_surface_coverage_percent=about 71
E037|grand_prismatic.diameter_feet=approximately 370;grand_prismatic.depth_feet=over 121
E038|travertine_terrace.deposited_mineral=calcite;yellowstone_travertine.source_rock=limestone
E039|grand_prismatic.basin=Midway Geyser Basin
E040|seawater.dissolved_salt_major_source=weathering of rocks on land
E041|tephra.size_range=ash through house sized boulders;volcanic_ash.particle_diameter_mm=less than 2
E042|metamorphic_rock.formation=existing rock altered by heat pressure or mineral rich fluids
E043|ocean_surface_salinity.latitudinal_pattern=higher mid latitudes and lower equator and poles
E044|water_table.excessive_well_pumping_effect=lowers water table
E045|ocean_sound_channel.propagation=refraction up and down within channel
E046|yellowstone_mudpot.clay_formation=sulfuric acid breaks down rock
S001|planet.venus.mean_temperature_c=464;planet.mars.mean_temperature_c=-65
S002|planet.earth.mass_10e24_kg=5.97;planet.mars.mass_10e24_kg=0.642
S003|planet.neptune.ring_system=yes;planet.mars.ring_system=no
S004|planet.mercury.length_of_day_hours=4222.6;planet.earth.length_of_day_hours=24.0
S005|si.length.base_unit=metre
S006|si.thermodynamic_temperature.base_unit=kelvin
S007|si_prefix.kilo.symbol=k
S008|element.iron.symbol=Fe;element.fluorine.symbol=F
S009|element.carbon.atomic_number=6;element.nitrogen.atomic_number=7
S010|element.gold.symbol=Au;element.silver.symbol=Ag
S011|planet.earth.density_kg_m3=5514;planet.venus.density_kg_m3=5243
S012|planet.neptune.escape_velocity_km_s=23.5;planet.uranus.escape_velocity_km_s=21.3
S013|planet.mercury.orbital_eccentricity=0.206;planet.mars.orbital_eccentricity=0.094
S014|planet.jupiter.rotation_period_hours=9.9;planet.saturn.rotation_period_hours=10.7
S015|si.kilogram.defining_constant=Planck constant
S016|si_prefix.nano.factor=10^-9;si_prefix.micro.factor=10^-6
S017|si_prefix.giga.factor=10^9;si_prefix.mega.factor=10^6
S018|element.zinc.atomic_number=30;element.copper.atomic_number=29
S019|element.aluminium.standard_atomic_weight=26.982;element.magnesium.standard_atomic_weight=24.305
S020|element.selenium.atomic_number=34;element.bromine.atomic_number=35
S021|planet.earth.diameter_km=12756;planet.venus.diameter_km=12104;planet.uranus.diameter_km=51118;planet.neptune.diameter_km=49528
S022|planet.saturn.orbital_period_days=10747;planet.uranus.orbital_period_days=30589;planet.neptune.orbital_period_days=59800;planet.saturn.mean_temperature_c=-140;planet.uranus.mean_temperature_c=-195;planet.neptune.mean_temperature_c=-200
S023|planet.earth.gravity_m_s2=9.8;planet.jupiter.gravity_m_s2=23.1;planet.neptune.gravity_m_s2=11.0
S024|planet.uranus.obliquity_degrees=97.8;planet.venus.obliquity_degrees=177.4;planet.uranus.orbital_inclination_degrees=0.8;planet.venus.orbital_inclination_degrees=3.4
S025|si_prefix.kilo.factor=10^3;si_prefix.giga.factor=10^9;si_prefix.mega.factor=10^6
S026|si.electric_current.base_unit=ampere;si.ampere.defining_constant=elementary charge
S027|si_prefix.mega.factor=10^6;si_prefix.micro.factor=10^-6;si_prefix.kilo.factor=10^3
S028|element.silver.atomic_number=47;element.iodine.atomic_number=53;element.gold.atomic_number=79;element.carbon.atomic_number=6
S029|element.silver.atomic_number=47;element.cadmium.atomic_number=48;element.indium.atomic_number=49;element.cadmium.standard_atomic_weight=112.41;element.indium.standard_atomic_weight=114.82
S030|element.tellurium.atomic_number=52;element.iodine.atomic_number=53;element.tellurium.standard_atomic_weight=127.60;element.iodine.standard_atomic_weight=126.90
S031|moon.length_of_day_hours=708.7;planet.mars.length_of_day_hours=24.7
S032|si_prefix.micro.symbol=mu;si_prefix.milli.symbol=m
S033|element.lead.symbol=Pb;element.phosphorus.symbol=P
S034|planet.saturn.diameter_km=120536;planet.uranus.diameter_km=51118
S035|planet.mercury.mean_temperature_c=167;planet.mars.mean_temperature_c=-65
S036|si_constant.avogadro.unit=mol^-1;si_constant.planck.unit=joule second
S037|si_prefix.ronto.factor=10^-27;si_prefix.yocto.factor=10^-24
S038|element.silver.atomic_number=47;element.cadmium.atomic_number=48
S039|planet.venus.orbital_velocity_km_s=35.0;planet.earth.orbital_velocity_km_s=29.8
S040|planet.neptune.gravity_m_s2=11.0;planet.saturn.gravity_m_s2=9.0
S041|si.luminous_intensity.base_unit=candela;si.amount_of_substance.base_unit=mole
S042|si_constant.luminous_efficacy.value_lm_w=683;si_constant.speed_of_light.value_m_s=299792458
S043|si_prefix.ronna.factor=10^27;si_prefix.quetta.factor=10^30
S044|element.tungsten.atomic_number=74;element.tantalum.atomic_number=73
S045|element.platinum.standard_atomic_weight=195.08;element.gold.standard_atomic_weight=196.97
S046|element.xenon.atomic_number=54;element.krypton.atomic_number=36
`.trim();
const catalog={},itemAtoms={};
for(const line of facts.split('\n')){
  const [id,s]=line.split('|');
  if(!byId[id])throw Error('Unknown '+id);
  itemAtoms[id]=s.split(';').map(part=>{
    const cut=part.indexOf('='),factId='fact:'+part.slice(0,cut),value=part.slice(cut+1);
    if(catalog[factId]&&catalog[factId].value!==value)throw Error('Atom value conflict '+factId);
    if(!catalog[factId])catalog[factId]={id:factId,property:part.slice(0,cut),value,ledger_item_ids:[]};
    catalog[factId].ledger_item_ids.push(id);
    return factId;
  });
}
if(Object.keys(itemAtoms).length!==rows.length)throw Error('Incomplete atoms');
const normalize=u=>u.replace(/\?.*$/,'').replace(/\/$/,'');
const groupBank=b=>b.startsWith('pilot')?'pilot':b;
const sourceCounts=rs=>Object.values(rs.reduce((a,r)=>{
 const k=normalize(r.source_url);a[k]??={source_page:k,count:0,item_ids:[]};a[k].count++;a[k].item_ids.push(r.id);return a;
},{})).sort((a,b)=>b.count-a.count||a.source_page.localeCompare(b.source_page));
const cross=[],within=[];
for(let i=0;i<rows.length;i++)for(let j=i+1;j<rows.length;j++){
 const a=rows[i],b=rows[j],shared=itemAtoms[a.id].filter(x=>itemAtoms[b.id].includes(x));
 if(!shared.length)continue;
 const overlap={item_ids:[a.id,b.id],banks:[a.bank,b.bank],shared_fact_atoms:shared,already_excluded_ids:[a,b].filter(x=>x.use_status==='EXCLUDE_PENDING_REPLACEMENT_2C').map(x=>x.id)};
 if(groupBank(a.bank)!==groupBank(b.bank))cross.push(overlap);
 else if(a.bank==='main'&&b.bank==='main')within.push(overlap);
}
const capReplace=['S001','S003','S011','S012','S014','S021','S023','S010','S019','S028','S030'];
const drop=['C027','C028','S017','S025','S027'];
const existingExcluded=rows.filter(r=>r.use_status==='EXCLUDE_PENDING_REPLACEMENT_2C').map(r=>r.id);
const otherAgent=['E021','E022','E023','E024','E025','E026','E027','E028','E029','E030','E033','E037','C024'];
const replaceMain=[...otherAgent.filter(id=>byId[id].bank==='main'),...capReplace,'C021'];
const keptOriginal=rows.filter(r=>r.bank==='main'&&!drop.includes(r.id)&&!replaceMain.includes(r.id));
const recommendedRemoval=new Set([...drop,...replaceMain,'S038','C044']);
const residualCross=cross.filter(x=>x.item_ids.every(id=>!recommendedRemoval.has(id)));
const residualWithin=within.filter(x=>x.item_ids.every(id=>!recommendedRemoval.has(id)));
const resolution={
 'C001|C021':'Keep C001; replace C021 to retain 85 main, or drop C021 for a lower-work 84-main option.',
 'C001|C044':'Keep C001; replace correction C044 with a wholly different fact.',
 'C021|C044':'Replace C021 and correction C044; replacing just C001 does not clear this pair.',
 'S001|S035':'Replace main S001 under NASA page cap; retain pilot S035.',
 'S021|S034':'Replace main S021 under NASA page cap; retain pilot S034.',
 'S023|S040':'Replace main S023 under NASA page cap; retain correction S040.',
 'S028|S038':'Replace S028 under IUPAC cap and replace already excluded pilot S038.',
 'S029|S038':'Retain main S029; replace already excluded pilot S038.'
};
for(const x of [...cross,...within])x.recommendation=resolution[x.item_ids.slice().sort().join('|')]||'Remove the already excluded member, or replace a member listed in the source-cap plan; see item recommendations.';
const items=rows.map(r=>({id:r.id,bank:r.bank,tier:r.tier,stem:r.stem,fact_atoms:itemAtoms[r.id],supporting_fact_atoms:r.id==='S006'?['fact:si.luminous_intensity.base_unit']:[],source_page:normalize(r.source_url),evidence:{ledger_file:'outputs/Authority Swap - Part 2b Source and Key Ledger.csv',source_url:r.source_url,locator:r.locator||r.source_locator,exact_excerpt:r.exact_excerpt,source_review_status:r.status},prior_use_status:r.use_status,recommendation:drop.includes(r.id)?'DROP_EXISTING_EXCLUSION':replaceMain.includes(r.id)?'REPLACE_MAIN':r.id==='S038'?'REPLACE_PILOT_EXISTING_EXCLUSION':r.id==='C044'?'REPLACE_CORRECTION_FACT_OVERLAP':r.id==='S006'?'REVISE_DISTRACTOR_FOR_STRICT_SUPPORTING_FACT_DISJOINTNESS':otherAgent.includes(r.id)?'REPLACE_ASSIGNED_TO_OTHER_AGENT':'KEEP_PROVISIONALLY'}));
const result={
 audit:'Authority Swap Part 2c independent fact-overlap and source-concentration audit',
 created_date:'2026-11-14',scope:'Read-only audit of the Part 2b source-reviewed originals. No model experiments, new literature, source-page browsing, or fresh verification performed. All replacement questions remain subject to independent fresh source/key checks.',
 input_files:['outputs/Authority Swap - Part 2b Source and Key Ledger.csv','outputs/Authority Swap - Part 2b Working Questions.csv'],
 input_integrity:{ledger_sha256:'B48550317011B1FF541CA525633ABCE2863097657C24B66B358396CFD34E3A7D',working_sha256:'FE0B5E444F0D2F8D2573C5CB2DE7C278F05CA0272228FA59F457DA977B5E7C4D',compared_fields:['id','bank','tier','stem','option_a','option_b'],row_counts:[138,138],question_field_differences:[]},
 atom_policy:{unit:'A proposition about an entity and one property, using stable semantic IDs. Numeric table cells for every compared candidate are separate atoms; identities include relevant alternative properties when source-derived exclusion needs them.',stem_facts:'Facts supplied in stems count as exposure and are included even for excluded arithmetic questions.',shared_page:'Sharing a page or entity is allowed when tested properties differ; shared pages alone are not factual overlap.',excerpt_boundary:'The full excerpt is retained as evidence, but unrelated clauses in an excerpt are not automatically treated as question atoms. This prevents broad source passages from collapsing distinct facts.',derived_facts:'Required source components are included for multi-step questions; direct source-explicit quantities need not include every possible alternate derivation.',supporting_boundary:'S006/S041 is an additional supporting/alternative-elimination overlap, although their target facts differ. Resolve conservatively for strict separation.',pilot_splits:'pilot_dev and pilot_accept are grouped as pilot for cross-bank comparisons; no shared core atom was found between those two subsets.'},
 summary:{original_items:138,original_main:90,original_pilot:24,original_correction:24,existing_excluded:existingExcluded.length,existing_excluded_ids:existingExcluded,additional_wording_flag:'C024',core_cross_bank_pairs:cross.length,within_main_redundant_pairs:within.length,source_page_cap:5,minimum_source_cap_main_replacements:11,main_after_dropping_five_existing_exclusions:85,main_if_also_drop_C021:84,main_if_replace_C021:85,total_if_85_main_and_all_48_other_bank_slots_preserved:133},
 source_counts:{original_main_distinct_pages:41,source_pass_unexcluded_main_distinct_pages:36,kept_original_main_distinct_pages:36,kept_original_max_items_per_page:5,all_original_main:sourceCounts(rows.filter(r=>r.bank==='main')),source_pass_unexcluded_main:sourceCounts(rows.filter(r=>r.bank==='main'&&r.use_status==='SOURCE_CHECKED_AWAITING_2C')),kept_original_main_before_new_replacements:sourceCounts(keptOriginal),final_source_counts:'Unknown until replacement drafts and fresh verification exist. Each replacement must be charged to its actual source page; do not assume a new URL is a new independent page.'},
 source_cap_plan:{NASA:{original_count:12,retain:['S002','S004','S013','S022','S024'],replace:['S001','S003','S011','S012','S014','S021','S023'],minimum_replacements:7},IUPAC:{original_count:9,retain:['S008','S009','S018','S020','S029'],replace:['S010','S019','S028','S030'],minimum_replacements:4},proof:'For a maximum of five items per page, twelve NASA items require at least seven removals/replacements, and nine IUPAC items require at least four. The proposed eleven meet this lower bound and clear the three NASA cross-bank pairs and IUPAC within-main numerical repeats.',S029_note:'Dropping its atomic-weight clause is optional for overlap; its atomic-number atoms are already disjoint from the other four retained IUPAC questions. Any clause deletion changes difficulty and requires fresh verification.'},
 cross_bank_overlaps:cross,
 supporting_fact_cross_bank_overlaps:[{item_ids:['S006','S041'],shared_fact_atom:'fact:si.luminous_intensity.base_unit',reason:'S006 ledger identifies candela as luminous-intensity unit to exclude it from thermodynamic-temperature units; S041 directly tests that mapping.',recommendation:'Revise S006 distractor or replace S041; independently verify any revised item. This is conservative supporting-fact overlap, not an exact target-fact duplicate.'}],
 within_main_redundancies:within,
 recommendations:{drop_main_ids:drop,assigned_replacements_other_agent:otherAgent,additional_source_cap_main_replacement_ids:capReplace,additional_main_replacement_for_85:'C021',additional_correction_replacement_ids:['C044'],additional_pilot_replacement_ids:['S038'],additional_distractor_revision_ids:['S006'],main_new_replacement_slots:replaceMain.length,retained_original_main_count:keptOriginal.length,main_count_after_23_new_replacements:keptOriginal.length+replaceMain.length,minimal_lower_work_option:'Keep the same plan but drop C021 instead of replacing it: 84 main. This is the smallest additional deletion after source-cap changes and already excluded drops.',fresh_verification:'Every replacement and substantive revision must receive a new source-derived key, supporting passage, false-alternative check and renewed atom check before use. This audit accepts no as-yet-unseen draft.'},
 retained_original_residual_checks:{core_cross_bank_overlap_pairs:residualCross,within_main_redundant_pairs:residualWithin,supporting_pair_still_needs_revision:['S006','S041'],unseen_new_questions_audited:false},
 tier_implications:{retained_original_main:{easy:27,medium:25,hard:10},final_85_if_replacement_slots_preserve_original_tiers:{easy:30,medium:29,hard:26},final_84_if_C021_dropped_and_other_slots_preserve_tiers:{easy:30,medium:29,hard:25},caution:'These are slot counts only, not verified difficulty ratings. A reduced 84/85 candidate plan explicitly abandons the original target of 30 usable main candidates per tier. Independently assess replacement difficulty rather than inheriting labels automatically.'},
 allowed_same_source_examples:[{ids:['C003','C014','C015','C032','C041'],reason:'Printing city, partner, vellum fraction, line-count name and language are different properties.'},{ids:['C006','C017','C042'],reason:'RNA base membership, backbone sugar and strandedness are distinct.'},{ids:['C026','C038'],reason:'Transcontinental call date and city endpoints are distinct.'},{ids:['S016','S032'],reason:'Micro multiplying factor and micro symbol are distinct properties; S032 does not test 10^-6.'},{ids:['C029','C035'],reason:'Amino-acid codon count and UAG membership in stop codons are distinct.'},{ids:['S010','S028','S045'],reason:'Gold symbol, atomic number and atomic weight are distinct properties; S010/S028 are removed for other reasons.'}],
 caveats:['Fact disjointness is stricter than stem uniqueness but does not guarantee statistical independence of questions sharing topics.','Source-page cap is assessed for main items only; no accidental cap is imposed on an institution or entire domain.','This fact audit does not certify distractor plausibility, tier balance, difficulty or final eligibility.','C024 source endpoint ambiguity remains until its replacement is independently verified.','C013 construction-start value is source-specific; the ledger reports other NPS dates but both precede pedestal construction.','Grand Canyon numeric ages are the cited approximate 2020 table values, not immutable ages.'],
 fact_catalog:Object.values(catalog),items
};
fs.writeFileSync(path.join(dir,'p2c-fact-audit.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({items:items.length,atoms:Object.keys(catalog).length,cross_pairs:cross.map(x=>x.item_ids),within_main_pairs:within.map(x=>x.item_ids),retained_original_main:keptOriginal.length,new_main:replaceMain.length,final_main:keptOriginal.length+replaceMain.length,residual_core_cross:residualCross.length,residual_core_within:residualWithin.length},null,2));
