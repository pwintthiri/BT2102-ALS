SELECT * from Members;
SELECT * from Book;
SELECT * from Reservation;
SELECT * from Fine;
SELECT * from Authors;
SELECT * from Temporary;


#13. display books on reservation 
SELECT  r.accessionNumber, b.title, r.membershipID, m.memberName
FROM Members m, Book b, Reservation r
WHERE r.membershipID = m.membershipID AND b.accessionNumber = r.accessionNumber;

#12. display books on loan
SELECT b.accessionNumber, b.title, GROUP_CONCAT(a.authorName SEPARATOR ", "), b.isbn, b.publisher, b.publicationYear 
FROM Book b, Authors a
WHERE b.membershipID IS NOT NULL AND b.accessionNumber = a.accessionNumber
GROUP BY a.accessionNumber;

#14. display members who have outstanding fines
SELECT f.membershipID, m.memberName, m.faculty, m.phoneNumber,m.emailAddress 
FROM Fine f, Members m
WHERE f.PaymentAmount > 0 AND m.membershipID = f.membershipID;

#15. display books on loan given membershipID
SELECT b.accessionNumber, b.title, GROUP_CONCAT(a.authorName SEPARATOR ", "),b.isbn, b.publisher, b.publicationYear 
FROM Book b, Authors a 
WHERE b.membershipID = "A101A" AND b.accessionNumber = a.accessionNumber
GROUP BY a.accessionNumber;

#10. book search 
SELECT b.accessionNumber, b.title, GROUP_CONCAT(a.authorName SEPARATOR ", "), b.isbn, b.publisher, b.publicationYear
FROM Book b, Authors a
WHERE b.publisher LIKE '%2009%' AND a.accessionNumber = b.accessionNumber
GROUP BY b.accessionNumber;