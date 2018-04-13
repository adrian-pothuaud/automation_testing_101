
/**
 * This class is generated automatically by Katalon Studio and should not be modified or deleted.
 */


def static "cura.Auth.login"(
    	Object username	
     , 	Object password	) {
    (new cura.Auth()).login(
        	username
         , 	password)
}

def static "cura.Appointment.create"(
    	Object facility	
     , 	Object apply_readmission	
     , 	Object healthcare_program	
     , 	Object visit_date	
     , 	Object comment	) {
    (new cura.Appointment()).create(
        	facility
         , 	apply_readmission
         , 	healthcare_program
         , 	visit_date
         , 	comment)
}
