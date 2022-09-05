USE Library;


CREATE TABLE Members(  
     membershipID       VARCHAR(6)    NOT NULL,
     memberName         VARCHAR(30),   
     faculty            VARCHAR(15), 
     phoneNumber	    VARCHAR(10),
     emailAddress	    VARCHAR(25),
	 PRIMARY KEY (membershipID));


	 
CREATE TABLE Book(
     accessionNumber    VARCHAR(5)    NOT NULL,
     title              VARCHAR(65),
     isbn               VARCHAR(15),
     publisher          VARCHAR(40),
	 publicationYear    SMALLINT, 
     membershipID 		VARCHAR(6),
     borrowDate			DATE,		
     dueDate			DATE,	 
     returnDate			DATE,
     
	 PRIMARY KEY (accessionNumber),
	 FOREIGN KEY (membershipID)   REFERENCES Members(MembershipID) ON DELETE CASCADE);
    
     
CREATE TABLE Reservation( 
     accessionNumber    VARCHAR(5)    NOT NULL,
     membershipID       VARCHAR(6)    NOT NULL,
     reserveDate        DATE,
     PRIMARY KEY (accessionNumber, membershipID)); 
     
CREATE TABLE Fine(
     membershipID       VARCHAR(6)    NOT NULL,
     paymentDate        DATE, 
     paymentAmount      SMALLINT,
	 PRIMARY KEY (membershipID));
     

CREATE TABLE Authors(
	authorName          VARCHAR(50)  NOT NULL,
    accessionNumber     VARCHAR(5),
    PRIMARY KEY (authorName, accessionNumber),
    FOREIGN KEY (accessionNumber)   REFERENCES Book(accessionNumber) ON DELETE CASCADE);

CREATE TABLE Temporary(
	membershipID 	VARCHAR(6) 	 NOT NULL,
    PRIMARY KEY (membershipID));

