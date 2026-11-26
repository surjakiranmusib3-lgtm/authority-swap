const fs=require('fs'),path=require('path'),crypto=require('crypto');
const dir=__dirname;
const read=n=>JSON.parse(fs.readFileSync(path.join(dir,n),'utf8').replace(/^\uFEFF/,''));
const old=read('p2c-fact-audit.json'),original=read('p2c-fact-audit-ledger-input.json');
const originalById=Object.fromEntries(original.map(r=>[r.id,r]));
const rows=read('p2c-final-fact-audit-input.json');
const c016=read('p2c-final-fact-audit-amended-c016.json');
const previewC016={...rows.find(r=>r.id==='C016')};
Object.assign(rows.find(r=>r.id==='C016'),c016);
const oldItems=Object.fromEntries(old.items.map(r=>[r.id,r]));
const catalog=Object.fromEntries(old.fact_catalog.map(f=>[f.id,{id:f.id,property:f.property,proposition:f.property.replaceAll('_',' ').replaceAll('.',' / ')+' = '+f.value,value:f.value,evidence_basis:'Part 2b source-reviewed ledger; inherited proposition, not freshly verified here',item_ids:[]} ]));
const atomLists=Object.fromEntries(rows.map(r=>[r.id,[...oldItems[r.id].fact_atoms]]));
function unresolved(item,id,proposition,candidateValues,role='answer_discriminating'){
 const factId='fact:'+id;
 catalog[factId]={id:factId,property:id,proposition,value:null,candidate_values:candidateValues,role,evidence_basis:'Required proposition inferred from candidate wording; value deliberately unresolved in this audit',item_ids:[]};
 return factId;
}
function set(item,defs){atomLists[item]=defs.map(d=>unresolved(item,...d));}
set('S001',[['standard_model.electromagnetic_force.carrier','The Standard Model particle that carries the electromagnetic force',['photon','gluon']]]);
set('S003',[['taj_mahal.commissioning_emperor','The Mughal emperor who commissioned the Taj Mahal',['Akbar','Shah Jahan']]]);
set('S010',[['platypus.reproduction_egg_laying','Whether platypuses lay eggs',[true,false]],['wombat.reproduction_egg_laying','Whether wombats lay eggs',[true,false]]]);
set('S011',[['ipv6.address_bit_length','The number of bits in an IPv6 address',[64,128]]]);
set('S012',[['accelerator.dipole_magnet_role','The principal role of dipole magnets in a circular particle accelerator',['beam bending','beam focusing']]]);
set('S014',[['angkor.location_country','The country containing the Angkor archaeological site',['Thailand','Cambodia']]]);
set('S019',[['human_circadian_clock.evening_sleepiness_hormone','The hormone increased in the evening by the human circadian clock to promote sleepiness',['melatonin','cortisol']]]);
set('C021',[['nobel_chemistry_1911.curie_isolated_element_citation','The element whose isolation is specifically credited in Marie Curie\'s 1911 Nobel Chemistry citation',['polonium','radium']]]);
set('C024',[['rosetta_stone.decree_ruler','The ruler concerned by the priestly decree on the Rosetta Stone',['Ptolemy V','Ptolemy III']]]);
set('E021',[['moho.boundary','The Earth-layer boundary marked by the Mohorovicic discontinuity',['crust to mantle','mantle to core']]]);
set('E022',[['turbidite_sandstone.bed_upward_grain_size_change','The usual grain-size change upward within a typical turbidite sandstone bed',['coarser','finer']]]);
set('E023',[['calcite.cleavage_geometry','The cleavage geometry characteristic of calcite',['rhombohedral','cubic']]]);
set('E024',[['kyanite.crystal_system','The crystal system of kyanite',['monoclinic','triclinic']]]);
set('E025',[['anchorage_benioff_zone.earthquake_host_plate','The tectonic plate principally hosting Benioff-zone earthquakes in the Anchorage region',['Pacific plate','North American plate']]]);
set('E026',[['spodic_material.characteristic_accumulation','The accumulation characteristic of spodic material in a soil profile',['calcium carbonate with gypsum','organic matter with aluminum']]]);
set('E027',[['regelation.glacier_obstacle_mechanism','How regelation helps glacier ice pass small bed obstacles',['pressure-driven melting and refreezing','plastic deformation without phase change']]]);
set('E028',[['solar_halo.characteristic_cloud_genus','The cloud genus characteristic of a halo around the Sun as seen from the ground',['Altostratus','Cirrostratus']]]);
set('E029',[['glacier.equilibrium_line_zero_quantity','The quantity that is zero at a glacier equilibrium line',['net mass balance','downslope velocity']]]);
set('E030',[['postglacial_scotland.isostatic_recovery_change','The physical change meant by postglacial isostatic recovery in Scotland',['ocean rises due to released glacial water','land rises after ice load removal']]]);
set('S021',[['unicode.nfkc.decomposition_and_composition','The decomposition and composition used by Unicode NFKC',['compatibility decomposition then canonical composition','canonical decomposition then canonical composition']],['unicode.nfc.decomposition_and_composition','The decomposition and composition used by Unicode NFC',['compatibility decomposition then canonical composition','canonical decomposition then canonical composition']]]);
set('S023',[['nobel_chemistry_2022.recognized_development','The development recognized by the 2022 Nobel Prize in Chemistry',['click and bioorthogonal chemistry','asymmetric organocatalysis']]]);
set('S028',[['rosetta_stone.middle_section_script','The script in the middle section of the Rosetta Stone',['Hieratic','Demotic']]]);
atomLists.S029=atomLists.S029.filter(id=>!id.includes('standard_atomic_weight'));
set('S030',[['tordesillas_treaty.signing_year','The year in which the Treaty of Tordesillas was signed',[1494,1496]]]);
set('E033',[['glacial_lake_varve.clay_richer_season','The season whose glacial-lake varve layer is typically richer in clay-sized sediment',['non-melting winter','melting summer']]]);
set('C037',[['cell.protein_lipid_processing_packaging_organelle','The organelle that helps process and package proteins and lipids for export',['mitochondrion','Golgi apparatus']]]);
set('S038',[['book_of_kells.gospel_language','The language of the four Gospels in the Book of Kells',['Greek','Latin']]]);
set('C038',[['titan.first_successful_landing_probe','The probe that made the first successful landing on Titan',['Huygens','Galileo']]]);
set('E037',[['foehn_drawdown.descending_air_warming_mechanism','The process chiefly warming descending air in the foehn draw-down mechanism',['expansion at lower pressure','compression at higher pressure']]]);
set('C044',[['wright_flyer_1903.engine_builder','The person who built the engine for the Wright brothers\' 1903 Flyer',['Charles Taylor','Glenn Curtiss']]]);
// Revised distractors: relevant elimination facts are tracked separately from target facts.
const supporting=Object.fromEntries(rows.map(r=>[r.id,[]]));
supporting.S006=[unresolved('S006','si.time.base_unit','The SI base unit for time',['second'],'alternative_elimination')];
supporting.E034=[unresolved('E034','breccia.rock_class','The class of sedimentary rock to which breccia belongs',['clastic','biologic'],'alternative_elimination')];
// C016 formerly disclosed the answer to C004; the audited overlay removes the year.
const stemDisclosures={C029:[{property:'genetic_code.codon_count',value:64}],C016:[]};
const eventIds={
 C001:['event:yellowstone_establishment'],C004:['event:bell_first_telephone_patent_grant'],C009:['event:bell_first_telephone_call'],
 C013:['event:statue_france_construction_start','event:statue_pedestal_construction_start'],C016:['event:bell_first_telephone_patent_grant'],
 C021:['event:curie_1911_nobel_chemistry_award'],C022:['event:lake_hotel_construction','event:old_faithful_inn_opening'],
 C026:['event:first_transcontinental_telephone_call','event:bell_patent_priority_supreme_court_decision'],
 C031:['event:yosemite_grant','event:yosemite_national_park_designation'],C033:['event:statue_replacement_torch_installation_1986'],
 C034:['event:corps_discovery_departure'],C038:['event:huygens_titan_landing'],C040:['event:statue_dedication'],
 C044:['event:wright_flyer_1903_engine_construction'],C045:['event:statue_original_torch_museum_relocation_2018'],
 S003:['event:taj_mahal_commission'],S023:['event:2022_nobel_chemistry_award'],S030:['event:tordesillas_treaty_signing']};
function norm(raw){const u=new URL(raw);u.hostname=u.hostname.toLowerCase().replace(/^www\./,'');if(u.hostname==='home.nps.gov')u.hostname='nps.gov';for(const key of [...u.searchParams.keys()])if(key.startsWith('utm_')||key.startsWith('qt-'))u.searchParams.delete(key);u.hash='';u.pathname=u.pathname.replace(/\/$/,'');return u.toString().replace(/\/$/,'');}
function sourceCounts(rs){return Object.values(rs.reduce((a,r)=>{const k=norm(r.source_url);a[k]??={source_page_id:k,count:0,item_ids:[]};a[k].count++;a[k].item_ids.push(r.id);return a;},{})).sort((a,b)=>b.count-a.count||a.source_page_id.localeCompare(b.source_page_id));}
const bankGroup=b=>b.startsWith('pilot')?'pilot':b;
const pairFacts=(rs,lists,predicate)=>{const out=[];for(let i=0;i<rs.length;i++)for(let j=i+1;j<rs.length;j++){const a=rs[i],b=rs[j];if(!predicate(a,b))continue;const ids=lists[a.id].filter(x=>lists[b.id].includes(x));if(ids.length)out.push({item_ids:[a.id,b.id],banks:[a.bank,b.bank],shared_fact_ids:ids});}return out;};
const allFacts=Object.fromEntries(rows.map(r=>[r.id,[...atomLists[r.id],...supporting[r.id]]]));
const cross=pairFacts(rows,allFacts,(a,b)=>bankGroup(a.bank)!==bankGroup(b.bank));
const within=pairFacts(rows,allFacts,(a,b)=>a.bank==='main'&&b.bank==='main');
const splitPilot=pairFacts(rows,allFacts,(a,b)=>a.bank.startsWith('pilot')&&b.bank.startsWith('pilot')&&a.bank!==b.bank);
const eventCross=pairFacts(rows,Object.fromEntries(rows.map(r=>[r.id,eventIds[r.id]||[]])),(a,b)=>bankGroup(a.bank)!==bankGroup(b.bank));
const changedQuestionIds=rows.filter(r=>['stem','option_a','option_b'].some(k=>r[k]!==originalById[r.id][k])).map(r=>r.id);
const newQuestionIds=['S001','S003','S010','S011','S012','S014','S019','C021','C024','E021','E022','E023','E024','E025','E026','E027','E028','E029','E030','S021','S023','S028','S030','E033','C037','S038','C038','E037','C044'];
const items=rows.map(r=>{
 const facts=atomLists[r.id],sup=supporting[r.id];
 for(const fid of [...facts,...sup]){if(!catalog[fid])throw Error('Missing '+fid);catalog[fid].item_ids.push(r.id);}
 return {id:r.id,bank:r.bank,tier:r.tier,stem:r.stem,option_a:r.option_a,option_b:r.option_b,source_url:r.source_url,source_locator:r.source_locator,source_page_id:norm(r.source_url),fact_atoms:facts.map(id=>({id,proposition:catalog[id].proposition,value:catalog[id].value,evidence_basis:catalog[id].evidence_basis})),supporting_fact_atoms:sup.map(id=>({id,proposition:catalog[id].proposition,value:catalog[id].value,evidence_basis:catalog[id].evidence_basis})),event_ids:eventIds[r.id]||[],explicit_stem_disclosures:stemDisclosures[r.id]||[],change_from_part2b:newQuestionIds.includes(r.id)?'replacement':changedQuestionIds.includes(r.id)?'revised_wording_or_options':'unchanged_question',fact_audit_status:'NO_RESIDUAL_FACT_DUPLICATE_FOUND',source_verification_status_in_this_audit:'NOT_PERFORMED',provenance:r.id==='C016'?'Amended adjudication CSV overlay; preview row is superseded. Fresh verification pending separately.':newQuestionIds.includes(r.id)?'New question requirements mapped without reading draft keys or deriving a verified answer.':'Previous ledger facts reused where unchanged; revisions are not certified by this audit.'};
});
const countsBefore=sourceCounts(original.filter(r=>r.bank==='main')),countsAfter=sourceCounts(rows.filter(r=>r.bank==='main'));
const afterMax=Math.max(...countsAfter.map(s=>s.count));
const hash=n=>crypto.createHash('sha256').update(fs.readFileSync(path.join(dir,n))).digest('hex').toUpperCase();
const result={
 audit:'Authority Swap Part 2c final candidate fact and event overlap audit',date:'2026-11-14',
 scope:'Content-level audit only. No source opening, new factual literature, blind key derivation, experimental model inference, hosted calls or credits. Source/key reviewers separately assess correctness. New propositions are unresolved requirements rather than newly verified facts.',
 inputs:{preview:'work/authority-swap/questions/p2c-candidate-preview.csv',preview_sha256:hash('p2c-candidate-preview.csv'),overlay:'C016 only from work/authority-swap/questions/p2c-adjudication-questions.csv',overlay_adjudication_file_sha256:hash('p2c-adjudication-questions.csv'),prior_fact_ledger:'work/authority-swap/questions/p2c-fact-audit.json',prior_source_ledger:'outputs/Authority Swap - Part 2b Source and Key Ledger.csv',important:'This audit applies to the saved 133-row preview plus the displayed C016 overlay, not an assertion that every other changing file or future assembly has been audited.',source_assembly_note:'Coordinator confirmed that final assembly starts from the Part2b source-reviewed ledger for unchanged rows, and replaces citations with actual fresh-review records where appropriate. Preview source URLs can be historical. E011 resolved DYFI source is preserved by assembly; C013 citation review is separate.'},
 summary:{items:items.length,main:85,pilot_dev:8,pilot_accept:16,correction:24,fact_atom_count:Object.values(catalog).filter(f=>f.item_ids.length).length,cross_bank_core_or_supporting_fact_pairs:cross.length,pilot_dev_accept_overlap_pairs:splitPilot.length,cross_bank_shared_event_pairs:eventCross.length,within_main_residual_fact_pairs:within.length,source_page_main_max_before:Math.max(...countsBefore.map(s=>s.count)),source_page_main_max_after:afterMax,main_source_cap:5,main_source_cap_pass:afterMax<=5,new_question_count:newQuestionIds.length,revised_or_replaced_question_count:changedQuestionIds.length,source_verification_performed:false},
 atom_policy:{meaning:'One entity-property proposition per canonical semantic ID. Comparisons include each relevant compared table cell. New answer values are intentionally unresolved. Alternative-elimination facts are tracked when they introduce a distinct meaningful property.',not_overlap:'A shared entity, answer string, topic, institution, source page or broad scientific process does not alone make two property propositions identical.',stem_information:'Explicit correct facts disclosed in a stem count as exposure. C016 was fixed because its year disclosed C004; C029 gives codon total64 but no other retained item tests that total.',event_rule:'No event is shared across banks in the enumerated historical-event map. Specifically the first transcontinental telephone call appears only in main C026; pilot C038 now concerns the Huygens landing.',source_identity:'URL host aliases www and home.nps are normalized; fragments and known tracking queries are ignored. Content-bearing query parameters such as object id and section are retained.'},
 cross_bank_residuals:cross,within_main_residuals:within,pilot_split_residuals:splitPilot,cross_bank_event_residuals:eventCross,
 resolved_findings:[
 {id:'FINAL-F001',ids:['C004','C016'],kind:'within_main_explicit_stem_disclosure',preview_problem:'Preview C016 supplied 1876, the answer to C004.',resolution:'Use amended C016: '+c016.stem,preview_stem:previewC016.stem,status:'CONTENT_OVERLAP_RESOLVED_BY_OVERLAY; FRESH_VERIFICATION_PENDING'},
 {id:'FINAL-F002',ids:['C026','C038'],kind:'cross_bank_shared_event',resolution:'C038 now tests the first successful probe landing on Titan. No first-transcontinental-call event remains outside C026.',status:'CONTENT_OVERLAP_RESOLVED'},
 {id:'FINAL-F003',ids:['S006','S041'],kind:'cross_bank_supporting_fact',resolution:'S006 now contrasts kelvin with second; candela/luminous-intensity mapping is confined to S041.',status:'CONTENT_OVERLAP_RESOLVED'},
 {id:'FINAL-F004',ids:['S029','S038'],kind:'cross_bank_atomic_number',resolution:'S038 now tests Book of Kells language; silver/cadmium atomic-number relationship remains only in S029.',status:'CONTENT_OVERLAP_RESOLVED'},
 {id:'FINAL-F005',ids:['C001','C021','C044'],kind:'repeated_yellowstone_year',resolution:'C021 now concerns Curie citation and C044 Wright Flyer engine builder; establishment1872 remains only C001.',status:'CONTENT_OVERLAP_RESOLVED'}],
 nuanced_same_entity_distinct_property_decisions:[
 {ids:['E023','E038'],entity:'calcite',decision:'ALLOW',reason:'E023 tests cleavage geometry of an identified mineral. E038 tests which mineral is deposited in travertine terraces. Neither stem supplies the other answer.'},
 {ids:['C024','S028'],entity:'Rosetta Stone',decision:'ALLOW_WITHIN_MAIN',reason:'The decree ruler and the middle-section script are distinct properties. Same artifact and two sources do not create factual duplication; topic clustering should still be disclosed.'},
 {ids:['C033','C045'],entity:'Statue of Liberty torches',decision:'ALLOW_DISTINCT_EVENTS',reason:'Replacement-torch installation in1986 and original-torch museum relocation in2018 are different objects/events. C037 was replaced with Golgi content, satisfying the requested diversification of at least one C033/C037 item.'},
 {ids:['C004','C016'],entity:'Bell telephone patent',decision:'ALLOW_AFTER_C016_OVERLAY',reason:'Grant year and patent number are distinct main-bank properties. Removing1876 from C016 prevents direct disclosure. The shared event is confined to main.'},
 {ids:['S016','S032'],entity:'micro prefix',decision:'ALLOW',reason:'Multiplying factor10^-6 and symbol mu are different columns/properties. The prompt for S032 does not disclose the exponent.'},
 {ids:['S002','S013','S031','S035'],entity:'Mars',decision:'ALLOW',reason:'Mass, orbital eccentricity, length of day and temperature are distinct properties. No Mars temperature item remains in main.'},
 {ids:['S022','S034','S040'],entity:'Saturn/Uranus/Neptune',decision:'ALLOW',reason:'Main S022 asks orbital period/temperature; pilot S034 diameter; correction S040 gravity. No numeric table cell is reused across these items.'},
 {ids:['C003','C014','C015','C032','C041'],entity:'Gutenberg Bible',decision:'ALLOW',reason:'Printing city, partner, vellum fraction, line-count name and language are distinct.'},
 {ids:['S038','C041'],entity:'different books with same candidate language',decision:'ALLOW',reason:'Book of Kells language and Gutenberg Bible language concern different objects; an equal answer string is not a shared fact.'},
 {ids:['C006','C017','C042'],entity:'RNA',decision:'ALLOW',reason:'Canonical base membership, backbone sugar and usual strandedness differ.'},
 {ids:['C018','C019','C037','C039'],entity:'gene expression and cellular transport',decision:'ALLOW',reason:'Transcription product, translation location, organelle processing/packaging and messenger-RNA information transport are distinct operations/properties.'},
 {ids:['C029','C035'],entity:'genetic code',decision:'ALLOW',reason:'Amino-acid-codon count and whether UAG is a stop signal are distinct; the latter does not expose the former count.'},
 {ids:['E022','E033'],entity:'sediment grain size',decision:'ALLOW',reason:'Vertical grading within a turbidite bed and seasonal clay concentration in a varve are different depositional contexts and propositions.'},
 {ids:['E031','E044'],entity:'groundwater/water table',decision:'ALLOW',reason:'Saturated-zone identity versus response of water-table level to excessive pumping.'},
 {ids:['E010','E038','E046'],entity:'Yellowstone hydrothermal features',decision:'ALLOW',reason:'Geyser plumbing, travertine mineral deposition and mudpot acid weathering are different feature mechanisms.'},
 {ids:['S015','S036'],entity:'Planck constant',decision:'ALLOW',reason:'Which constant defines kilogram and the constant\'s dimensional unit are distinct properties; S036 contrasts Avogadro/Planck units.'}
 ],
 source_concentration:{before_main_total:90,after_main_total:85,before_distinct_pages:countsBefore.length,after_distinct_pages:countsAfter.length,before:countsBefore,after:countsAfter,over_cap_after:countsAfter.filter(s=>s.count>5),NASA_final_ids:['S002','S004','S013','S022','S024'],IUPAC_final_ids:['S008','S009','S018','S020','S029'],known_assembly_source_override:{id:'E011',source_url:originalById.E011.source_url,concentration_effect:'Singleton page replaced by another singleton page; main distinct count59 and maximum5 unchanged.'},interpretation:'Main cap5 passes for the audited preview plus C016. Cross-bank page reuse is allowed when facts differ. This does not certify source reliability or imply institutional independence. Final assembly should recalculate using actual accepted reviewer citations.'},
 quality_observations:[
 {ids:['E040'],severity:'LOW',type:'distractor_plausibility',observation:'Evaporation creating new dissolved salts is categorically implausible to knowledgeable respondents; this item may be easier than medium. No source-independent logical tautology is introduced, and this is not a factual-overlap blocker.'},
 {ids:['S014','S030','C038','E029'],severity:'LOW',type:'provisional_difficulty',observation:'Several medium/hard items ask one direct fact; difficulty can rest on unfamiliarity, but labels should not be treated as empirically validated.'},
 {ids:['E021','E022','E023','E024','E025','E026','E027','E028','E029','E030','E033','E037'],severity:'INFO',type:'arithmetic_design_repair',observation:'Prior supplied-number arithmetic is gone; revised questions require factual identification or conceptual discrimination.'},
 {ids:['E011'],severity:'HANDLED_BY_ASSEMBLY_VALIDATION',type:'source_provenance',observation:'Preview E011 points to the original USGS FAQ; Part2b source-reviewed ledger used the accessible DYFI background page. Coordinator confirmed assembly preserves the resolved DYFI citation from the reviewed ledger. This audit made no new access attempt; final assembly validation remains separate.',preview_source:rows.find(r=>r.id==='E011').source_url,part2b_reviewed_source:originalById.E011.source_url},
 {ids:['C021'],severity:'VERIFY_SEPARATELY',type:'precise_source_scope',observation:'The question depends on the exact distinction between isolation and discovery in the1911 award citation; its correct answer is deliberately not derived here.'}
 ],
 final_assessment:'No residual cross-bank fact or enumerated-event overlap, or within-main shared proposition, was found after the amended C016 overlay. Main source cap5 passes. This is a content-audit conclusion contingent on the exact audited wording; correctness and final fresh-verification acceptance are separate.',
 fact_catalog:Object.values(catalog).filter(f=>f.item_ids.length),items
};
if(items.length!==133||cross.length||within.length||splitPilot.length||afterMax>5)throw Error('Audit invariant failed; inspect findings');
fs.writeFileSync(path.join(dir,'p2c-final-fact-audit.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({summary:result.summary,source_pages_before:countsBefore.length,source_pages_after:countsAfter.length,top_after:countsAfter.slice(0,6),new_question_ids:newQuestionIds,changed_question_ids:changedQuestionIds},null,2));
