CREATE TABLE Organization(
  Org_id int NOT NULL,
  Org_name varchar(20) NOT NULL,
  Location varchar(20),
  Government_approved int, # 0 or 1
  PRIMARY KEY(Org_ID)
);

CREATE TABLE Donor(
  Donor_id int NOT NULL,
  Donor_name varchar(20) NOT NULL,
  Phone_no varchar(20) NOT NULL,
  Org_id int NOT NULL,
  FOREIGN KEY(Org_ID) REFERENCES Organization(Org_ID) ON DELETE CASCADE ON UPDATE CASCADE,
  PRIMARY KEY(Donor_ID)
);

CREATE TABLE Patient(
  Patient_id int NOT NULL,
  Patient_name varchar(20) NOT NULL,
  Phone_no varchar(20) NOT NULL,
  organ_req varchar(20) NOT NULL,
  Location varchar(20),
  Org_id int NOT NULL,
  FOREIGN KEY(Org_ID) REFERENCES Organization(Org_ID) ON DELETE CASCADE ON UPDATE CASCADE,
  PRIMARY KEY(Patient_ID)
);
-- CREATE TABLE Patient(
--   Patient_id int NOT NULL,
--   Patient_name varchar(20) NOT NULL,
--   Phone_no varchar(20) NOT NULL,
--   organ_req varchar(20) NOT NULL,
--   Location varchar(20),
--   Org_id int NOT NULL,
--   FOREIGN KEY(Org_id) REFERENCES Organization(Org_ID) ON DELETE CASCADE ON UPDATE CASCADE,
--   PRIMARY KEY(Patient_ID)
-- );

CREATE TABLE Organ(
  Organ_ID int NOT NULL,
  Organ_name varchar(20) NOT NULL,
  Donor_ID int NOT NULL,
  Patient_ID int NOT NULL,
  FOREIGN KEY(Donor_ID) REFERENCES Donor(Donor_ID) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY(Patient_ID) REFERENCES Patient(Patient_ID) ON DELETE CASCADE ON UPDATE CASCADE,
  PRIMARY KEY(Organ_ID)
);


-- funtion
DELIMITER &&
CREATE procedure get_organizations_in_banglore()
BEGIN
select * from Organization where Location like "Banglore";
select COUNT(Location) AS total_no_of_organization from Organization;
END &&
DELIMITER ;



-- trigger
DELIMITER $$
CREATE TRIGGER update_organ
BEFORE INSERT ON Organ
FOR EACH ROW
IF NEW.Organ_name="Heart" THEN SET NEW.Organ_name="Multiple organs";
END IF;
END $$
DELIMITER ;




