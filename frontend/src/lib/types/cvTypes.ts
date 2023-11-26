import type { interestType } from "$lib/types/interestType";
import type { academicExperienceType } from "$lib/types/academicExperienceType";
import type { personalInformationType } from "$lib/types/personalInformationType";
import type { referenceType } from "$lib/types/referenceType";
import type { languageType } from "$lib/types/languageType";
import type { workExperienceType } from "$lib/types/workExperienceType";
import type { skillType } from "$lib/types/skillType";

export type cvTypes =
	| skillType
	| interestType
	| academicExperienceType
	| personalInformationType
	| referenceType
	| languageType
	| workExperienceType;
