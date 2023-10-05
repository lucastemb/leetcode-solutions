class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        m={}
        for email in emails: 
            domain=email.split('@')
            new_email=domain[0].replace('.','')
            if '+' in new_email:
                new_email=new_email[:new_email.find('+')]
            new_email+=("@"+domain[1])
            m[new_email]=1+m.get(new_email, 0)
        return len(m)
        