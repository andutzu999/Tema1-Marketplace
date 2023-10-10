

						TEMA 1 - Marketplace
		
		Organizare
		
			Rolul clasei Marketplace în implementarea temei este de a stoca produsele 
		aduse în market de către producatori și de a ține evidența produselor aflate
		în coșul fiecărui consumator. Am ales să stochez produsele aduse de producători
		în magazin într-un dicționar ce are ca și chei id-ul fiecaruia, valorile acestora
		fiind indexate. Avem un dictionar asemănător și pentru consumator, cart_id urile
		lor de data aceasta identifică coșurile acestora. Practic, rolul temei este de a
		simula o problemă Multi Producer Multi Consumer.
			
			Consider că tema este utilă deoarece te invață cum să folosești lock-uri
		care au un rol foarte important în organizarea execuției thread-urilor. Totodată,
		python este limbajul potrivit pentru implementarea acestui tip de problema.
			Implementarea mea este destul de bună si eficientă, avand in vedere faptul că
		nu depaseste limita de timp impusa in teste.
		
		
		Implementarea
		
			S-a implementat aproape tot enunțul temei, mai puțin o porțiune mică din pylint,
		pentru că am considerat că nu e necesar ca acesta sa fie perfect, fiind deja aproape de 
		perfecțiune. Nu există functionalități lipsă în temă.
			Am întâmpinat dificultăți în înțelegerea enuntului și a structurării informațiilor
		din fișierele de intrare. 
			Ceea ce am descoperit și mi s-a părut foarte interesant a fost faptul că atunci când 
		funcția de run din producator intră în sleep, în acel moment, un consumator poate lua 
		acel produs de pe raft. Mai pe scurt, am ințeles rolul introducerii sleep-ului îm temă. 
		
		
		Resurse utilizate
		
			Laboratorul 2 de asc
			
		Git:
			https://github.com/andutzu999/Tema1-Marketplace
			
