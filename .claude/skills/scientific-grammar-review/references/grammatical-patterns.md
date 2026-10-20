# Grammatical Patterns for Scientific Review

All examples below are original synthetic illustrations. A feature is not a
finding: report the identifiable defect in context. Suggested severity assumes
the example's local role; central scientific ambiguity may warrant major severity.
The alternatives illustrate grammar, not new scientific facts. Conditional
alternatives must not be substituted until the author establishes the meaning.

## Rule index

| ID | Phenomenon | Typical classification |
|---|---|---|
| GRAM-001 | Copular indirection | STYLE_PREFERENCE |
| GRAM-002 | Obscuring nominalization | CLARITY_PROBLEM |
| GRAM-003 | Modifier placement and attachment | CLARITY_PROBLEM |
| GRAM-004 | Anaphoric reference | CLARITY_PROBLEM |
| GRAM-005 | Syntactic parallelism | GRAMMATICAL_ERROR |
| GRAM-006 | Unnecessary relative clauses | STYLE_PREFERENCE |
| GRAM-007 | Coordination scope and constituent ambiguity | CLARITY_PROBLEM |
| GRAM-008 | Verb complementation | GRAMMATICAL_ERROR |
| GRAM-009 | Dangling participial modifiers | GRAMMATICAL_ERROR |
| GRAM-010 | Excessive embedding and discontinuity | CLARITY_PROBLEM |
| GRAM-011 | Redundant verbal periphrasis | STYLE_PREFERENCE |
| GRAM-012 | Clause linkage and sentence punctuation | GRAMMATICAL_ERROR |
| GRAM-013 | Information structure | CLARITY_PROBLEM |
| GRAM-014 | Subject–verb agreement | GRAMMATICAL_ERROR |
| GRAM-015 | Referential and semantic scope precision | CLARITY_PROBLEM |

Choose the most specific rule. GRAM-003 covers attachment except dangling
participles (009) and coordination (007). GRAM-015 covers remaining scope and
comparison ambiguity, not a second finding for those problems. Use GRAM-002 when
a process noun obscures participants, GRAM-011 for redundant verbal scaffolding.
Rule identifiers name phenomena, not fixed classifications: apply the definition
of the actual defect. Mixed grammatical categories alone do not prove an error.

### Rule GRAM-001: Copular indirection

**Definition:** A copular verb (such as *be*, *seem*, or *become*) links a subject
to a predicative subject complement. A nominal pro-form such as *one* can stand
for a noun phrase and carry a relative clause. Direct predication attributes a
property or action without that nominal scaffold.

**Why problematic:** A pro-form plus relative clause can delay a simple property
without adding classification, contrast, or reference.

**Detection:** Test whether the pro-form identifies an entity or class. Flag only
when it contributes no such distinction and the indirect predication has a local
readability cost or conflicts with an explicit direct-predication preference.

**Dispreferred:** The coating is one that resists moisture.

**Preferred:** The coating resists moisture.

**Structural explanation:** Promote the relative clause's lexical predicate to
the main clause; remove the copula and redundant nominal pro-form.

**Valid counterexample:** The pale band is the one that contains silver.

**Exceptions:** Identification, classification, contrastive focus, hedging, and
change of state justify copulas. Do not remove *seems* or *becomes*: epistemic
status and change of state are meaning. Copular syntax itself is grammatical.

**Classification / suggested severity:** STYLE_PREFERENCE / minor; CLARITY_PROBLEM
only when a specific relationship is obscured.

### Rule GRAM-002: Obscuring nominalization

**Definition:** Nominalization represents an action or property as a noun; a
deverbal noun derives from a verb. Light-verb constructions pair a relatively
low-content verb (for example, *perform*) with an event noun carrying much of the
predicate's meaning. Neither is intrinsically defective.

**Why problematic:** Converting processes into nouns can suppress agency or leave
relations among participants implicit in chains of *of* phrases.

**Detection:** Recover the event, agent, and affected entity. Flag only if their
relationship is genuinely unclear, or if redundant scaffolding has a demonstrable
cost. Do not invent an omitted agent to make an active clause.

**Dispreferred:** The measurement of the sample's heating by the technician was repeated.

**Preferred:** If the technician made the measurement: The technician's measurement of the sample's heating was repeated.

**Structural explanation:** Move the established measuring agent into a possessive
modifier of *measurement*. The original by-phrase could attach to either event
noun: the technician may have measured the heating or heated the sample. If the
intended agent is unknown, ask rather than selecting either interpretation.

**Valid counterexample:** The solution crystallized overnight. This crystallization reduced the dissolved fraction.

**Exceptions:** Event nouns support abstraction, technical naming, measurement,
and information structure (the organization of given and new information).
Preserve them when they maintain a topic or refer back to an established process.

**Classification / suggested severity:** CLARITY_PROBLEM / major for ambiguous
participants; STYLE_PREFERENCE / minor for merely cumbersome light-verb wording.

### Rule GRAM-003: Modifier placement and attachment

**Definition:** A modifier adds information to a head or larger constituent.
Attachment determines which constituent it modifies; scope determines the portion
of meaning affected. Prepositional and participial phrases can attach at more
than one syntactic level; restrictive modifiers delimit a referent's extension.

**Why problematic:** Placement may support competing relations or put an
unnecessary distance between a head and a restrictive modifier.

**Detection:** Identify plausible attachment sites and explain the consequential
readings. Use GRAM-009 for an introductory participial clause with no appropriate
controller. A difficult but valid attachment is a clarity issue, not an error.

**Dispreferred:** We measured the particles in the vial with a blue filter.

**Preferred:** If the filter was an instrument: Using a blue filter, we measured the particles in the vial.

**Structural explanation:** Move the instrumental phrase to a position where it
modifies the measuring event rather than appearing to describe the vial.

**Valid counterexample:** We measured the particles in the sealed vial.

**Exceptions:** Adjacency is not an absolute rule. Established technical phrases,
end-weight, and context can make an attachment clear. Do not move *only* or other
scope-bearing modifiers without checking the change in meaning.

**Classification / suggested severity:** CLARITY_PROBLEM / minor or major if the
instrument or sample identity changes. Reserve GRAMMATICAL_ERROR for an actual
syntactic incompatibility, not just ambiguity.

### Rule GRAM-004: Ambiguous anaphoric reference

**Definition:** Anaphora interprets an expression by reference to an antecedent in
the discourse. Pronouns (*it*, *they*) and demonstratives (*this*, *that*, *these*,
*those*, and *such*) can refer to entities, propositions, or events.

**Why problematic:** More than one plausible antecedent can obscure which entity
or result a claim concerns.

**Detection:** Read the surrounding sentences, enumerate plausible antecedents,
and determine whether the intended reference is recoverable. Do not require a
noun after every demonstrative. Check discourse reference rather than nearest-noun
matching alone.

**Dispreferred:** The pigment entered the solvent. It became unstable.

**Preferred:** If the pigment is intended: The pigment became unstable.

**Structural explanation:** Replace the pronoun with its established antecedent;
if unresolved, ask which entity became unstable.

**Valid counterexample:** All seeds germinated within a day. This was unexpected.

**Exceptions:** Demonstratives can clearly refer to an entire proposition. Dummy
*it* in *It is likely that...* has no nominal antecedent and is not faulty anaphora.
Technical noun repetition may be the most precise choice.

**Classification / suggested severity:** CLARITY_PROBLEM / major if the referent
changes a result, otherwise minor.

### Rule GRAM-005: Faulty syntactic parallelism

**Definition:** Coordination joins constituents through conjunctions. Parallelism
is correspondence in their syntactic function or form. Coordinate constituents
must fit their shared syntactic frame; they need not always share a category.

**Why problematic:** An incompatible shared frame makes the clause ungrammatical;
uneven but compatible structures may simply impede comparison.

**Detection:** Expand each coordinated member separately into the shared frame.
Check correlative conjunctions (*both...and*, *either...or*) and list structure.
Do not call every category mismatch an error.

**Dispreferred:** The procedure involves washing the film and to dry it.

**Preferred:** The procedure involves washing the film and drying it.

**Structural explanation:** *Involves* licenses the coordinated gerund-participial
complements, whereas the infinitival *to dry* does not fit that frame.

**Valid counterexample:** The layer is thin and of uniform composition.

**Exceptions:** The adjective phrase and prepositional phrase in the counterexample
both function as predicative complements. Rhetorical asymmetry can be legitimate.

**Classification / suggested severity:** GRAMMATICAL_ERROR / minor for incompatible
frames; CLARITY_PROBLEM only for a supported processing problem in valid syntax.

### Rule GRAM-006: Unnecessary relative clauses

**Definition:** A restrictive (integrated) relative clause narrows the nominal
referent; a nonrestrictive (supplementary) relative adds information about an
already identifiable referent. Relative pronouns connect the clause to its head.
Both introduce syntactic embedding.

**Why problematic:** A relative that contributes no needed distinction can delay
the predicate or duplicate information already encoded in the noun phrase.

**Detection:** Ask what distinction or new proposition the clause contributes.
Do not remove restrictions on the population to which a result applies.

**Dispreferred:** The powder, which is a powder with no detectable odor, was stored in glass.

**Preferred:** The odorless powder was stored in glass.

**Structural explanation:** Replace a redundant supplementary predication with an
attributive adjective, provided *odorless* has the same operational meaning here.
If it would imply a stronger claim, retain *with no detectable odor* instead.

**Valid counterexample:** The seedlings that received no nitrogen remained small.

**Exceptions:** Restrictive clauses identify subsets. Nonrestrictive clauses can
carry useful qualifications. Reduced relatives may hide agency, time, or modality;
do not remove these distinctions for economy.

**Classification / suggested severity:** STYLE_PREFERENCE / minor. Incorrect
restriction or punctuation that changes the population is a meaning issue.

### Rule GRAM-007: Coordination scope and constituent ambiguity

**Definition:** Constituent structure groups words into syntactic units.
Coordination scope determines which units a conjunction joins and whether a
modifier applies to one conjunct or the whole coordination.

**Why problematic:** Alternative bracketings can change the materials, treatment
groups, or relationships included in a scientific assertion.

**Detection:** Show at least two plausible groupings with materially different
meanings. Do not infer grouping from a serial comma alone.

**Dispreferred:** We compared heated salts and minerals.

**Preferred:** If both were heated: We compared heated salts and heated minerals.

**Structural explanation:** Repeat the shared modifier to make its scope over
both conjuncts explicit. If only salts were heated, specify that distinction.

**Valid counterexample:** We compared heated salts with unheated minerals.

**Exceptions:** Shared modifiers are efficient when context makes scope clear.
Repeated nouns or modifiers are justified to disambiguate. Do not add restrictions
such as *unheated* without evidence.

**Classification / suggested severity:** CLARITY_PROBLEM / major when grouping
affects scientific interpretation, otherwise minor.

### Rule GRAM-008: Incorrect verb complementation

**Definition:** Valency describes a predicate's licensed arguments. Argument
structure relates those arguments to participant roles; complementation specifies
the syntactic forms licensed by a particular verb or sense. Transitivity concerns
whether a construction takes a direct object.

**Why problematic:** An unlicensed object, preposition, infinitive, or clause can
break the construction or obscure participant roles.

**Detection:** Check the verb's actual sense and formal-English complementation
pattern. Distinguish objects, prepositional complements, and adjuncts. Verify
uncertain dialect or discipline-specific usage before calling it an error.

**Dispreferred:** The team discussed about the spectrum.

**Preferred:** The team discussed the spectrum.

**Structural explanation:** *Discuss* takes the topic as a direct object in this
sense; the preposition is not licensed in that frame.

**Valid counterexample:** The team agreed about the calibration procedure.

**Exceptions:** Different verbs and senses license different frames. Do not treat
all prepositions as redundant or demand objects after intransitive verbs.

**Classification / suggested severity:** GRAMMATICAL_ERROR / minor; major only if
participant roles or a central assertion become unrecoverable.

### Rule GRAM-009: Dangling participial modifiers

**Definition:** A supplementary participial clause often has an understood
subject controlled by the matrix-clause subject. A dangling modifier occurs when
the intended controller is absent or incompatible with that subject.

**Why problematic:** The syntax attributes an action or state to an unintended
entity, even if the reader can guess the actual agent.

**Detection:** Recover the participle's implied subject and compare it to the main
subject. Distinguish subject-oriented supplements from result clauses, absolutes,
and conventional expressions.

**Dispreferred:** While weighing the crystals, the balance stopped working.

**Preferred:** While the technician was weighing the crystals, the balance stopped working.

**Structural explanation:** Give the subordinate clause its own explicit subject;
the balance cannot be the intended agent of weighing. Use *technician* only if
that agent is established; otherwise retain an agent-neutral temporal clause.

**Valid counterexample:** Having cooled overnight, the liquid was filtered.

**Exceptions:** Passive main clauses can have an appropriate subject controller.
Absolute clauses (*the temperature remaining constant, ...*) have their own
subjects. Result supplements (*..., producing a dark residue*) need not describe
an intentional action by the matrix subject. Conventional *assuming that* and
*considering* constructions require contextual judgment.

**Classification / suggested severity:** GRAMMATICAL_ERROR / minor when clearly
dangling; CLARITY_PROBLEM when more than one controller remains plausible.

### Rule GRAM-010: Excessive embedding and discontinuity

**Definition:** Embedding places a clause within another constituent. Repeated
center embedding interrupts an enclosing dependency before it is completed.
Discontinuity separates syntactically related elements with intervening material.

**Why problematic:** Multiple unresolved dependencies can make the main
proposition hard to recover even in a grammatical sentence.

**Detection:** Identify the actual interrupted subject–predicate or head–modifier
dependencies. Consider reader needs, established terms, and context. Neither word
count nor subordinate-clause count alone establishes a defect.

**Dispreferred:** The grains that the solution that the chemist prepared dissolved were weighed.

**Preferred:** The chemist prepared a solution that dissolved the grains. Those grains were weighed.

**Structural explanation:** Externalize the inner dependency and explicitly retain
the restricted set of grains. A split is one option, not an obligation.

**Valid counterexample:** Although the signal weakened after sunset, the instrument recorded each pulse that exceeded the threshold, and the analysis retained those pulses for comparison.

**Exceptions:** Long, right-branching sentences can be easy to follow. Embedded
qualifications may be essential. Do not split away conditions or change their scope.

**Classification / suggested severity:** CLARITY_PROBLEM / minor, major if the
central proposition cannot reliably be recovered.

### Rule GRAM-011: Redundant verbal periphrasis

**Definition:** Verbal periphrasis expresses a predicate through multiple words,
including light verbs and auxiliary expressions. Indirect predication can realize
an action through a support phrase instead of a lexical verb.

**Why problematic:** Redundant support expressions can obscure the central action
and burden a local sequence without contributing aspect, modality, or contrast.

**Detection:** Substitute a direct predicate and check whether ability, intention,
completion, permission, evidence, or emphasis disappears. If it does, keep the
original or preserve that meaning explicitly.

**Dispreferred:** The solution undergoes the process of becoming cloudy.

**Preferred:** The solution becomes cloudy.

**Structural explanation:** Remove the redundant process scaffold while retaining
the inchoative predicate *becomes*, which expresses a change of state.

**Valid counterexample:** The larvae were able to survive the cold period.

**Exceptions:** Ability does not assert actual survival. Likewise *may cause* must
not become *causes*, and *attempted to measure* must not become *measured*. A
light-verb expression may be an established technical predicate.

**Classification / suggested severity:** STYLE_PREFERENCE / minor unless a
specific interpretive problem supports CLARITY_PROBLEM.

### Rule GRAM-012: Clause linkage and sentence punctuation

**Definition:** Independent clauses can stand as sentences; subordinate clauses
are grammatically dependent. Coordination joins comparable units, whereas
subordination marks dependency. Sentence punctuation signals these boundaries.

**Why problematic:** Fused sentences, comma splices, and unintended fragments
obscure boundaries. Conjunctions such as *since* can mark either time or cause.

**Detection:** Identify finite clauses and the licensed linkage. In standard formal
prose, a comma alone generally cannot join two independent declarative clauses.
Distinguish a grammatical boundary defect from an ambiguous logical connector.

**Dispreferred:** The gel expanded, the container cracked.

**Preferred:** The gel expanded. The container cracked.

**Structural explanation:** Mark independent sentence boundaries without asserting
that one event caused the other. A semicolon is also grammatical. If an author
prefers to avoid semicolons, use a valid alternative without inventing causality.

**Valid counterexample:** Because the exposure was brief, the film remained intact.

**Exceptions:** Deliberate fragments in headings, tables, and conventional labels
are legitimate. Rhetorical asyndeton is context-sensitive. *Since* is acceptable
when its temporal or causal reading is clear. Never replace *and* with *therefore*
without evidence of causation.

**Classification / suggested severity:** GRAMMATICAL_ERROR / minor for faulty
boundaries or unintended fragments; CLARITY_PROBLEM / major for consequential
causal/temporal ambiguity.

### Rule GRAM-013: Information structure

**Definition:** Topic is what a discourse segment is about; focus is information
presented as salient, contrasting, or new. Main and subordinate clauses and
subject position can distribute prominence, but syntax does not impose a single
universal given-before-new ordering.

**Why problematic:** A central answer may be buried in a subordinate clause while
the main clause repeats settled information, making the passage's function unclear.

**Detection:** Establish the question and preceding context. Explain the actual
mismatch in prominence. Without that context, do not diagnose a universal ordering
violation or assume that every subordinate result should be promoted.

**Dispreferred:** [Question: Did the treatment change leaf color?] The plants, which became purple after treatment, were kept in the already described trays.

**Preferred:** The plants became purple after treatment. They were kept in the already described trays.

**Structural explanation:** Promote the answer from a supplementary relative to a
main clause, retaining the temporal relationship rather than asserting causation.

**Valid counterexample:** [Topic: Storage conditions.] The samples, which contained trace copper, were stored in darkness.

**Exceptions:** Backgrounding, contrast, passive topic continuity, end-weight,
and disciplinary rhetorical conventions may justify the original organization.

**Classification / suggested severity:** CLARITY_PROBLEM / minor when the answer
is materially obscured; STYLE_PREFERENCE for an optional, explicitly grounded
prominence choice. Not GRAMMATICAL_ERROR.

### Rule GRAM-014: Subject–verb agreement

**Definition:** In finite clauses, the verb's person and number normally agree
with the subject. A complex subject's grammatical head, rather than an intervening
noun in a modifier, usually controls agreement.

**Why problematic:** Attraction to a nearby noun can produce a mismatched finite
verb and make the subject's structure harder to recognize.

**Detection:** Locate the finite verb and subject head, accounting for coordination,
existential constructions, notional agreement, and dialectal alternatives.

**Dispreferred:** The distribution of the droplets were uneven.

**Preferred:** The distribution of the droplets was uneven.

**Structural explanation:** The singular head *distribution* controls agreement;
plural *droplets* belongs to the embedded prepositional phrase.

**Valid counterexample:** The droplets and the surrounding vapor were analyzed separately.

**Exceptions:** Collective nouns permit dialect-dependent notional agreement.
*Data* may take singular or plural agreement according to disciplinary usage.
Measure phrases (*Ten minutes is sufficient*) can take singular agreement.

**Classification / suggested severity:** GRAMMATICAL_ERROR / minor unless number
ambiguity materially changes which scientific entity is asserted to have a property.

### Rule GRAM-015: Referential and semantic scope precision

**Definition:** Scope determines the interpretation domain of operators such as
negation, quantifiers, and comparison. Ellipsis leaves recoverable material
unexpressed. A construction is materially ambiguous when multiple plausible parses
or scope readings change the scientific relation.

**Why problematic:** An elliptical comparison may compare unlike entities, or
negation and quantifiers may support different conclusions.

**Detection:** Expand the alternative readings. Distinguish linguistic ambiguity
from information simply absent from the experiment description. Use the more
specific attachment, coordination, or anaphora rule when applicable.

**Dispreferred:** The density of the alloy exceeded the ceramic.

**Preferred:** If densities are compared: The density of the alloy exceeded that of the ceramic.

**Structural explanation:** Supply the comparative nominal head so that the
comparison relates two densities rather than a density and a material.

**Valid counterexample:** Not all cultures formed colonies.

**Exceptions:** The counterexample means that at least one culture did not form
colonies; it does not mean that none did. Preserve quantifier scope and uncertainty.
If a comparison's denominator or experimental condition is missing entirely,
request scientific clarification rather than inventing a grammatical correction.

**Classification / suggested severity:** CLARITY_PROBLEM / major for a changed
comparison or scope; minor for local recoverable imprecision.
