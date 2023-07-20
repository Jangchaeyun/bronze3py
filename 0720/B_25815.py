def cats_age(year, month):
    cat_age_year, cat_age_month = 0, 0
    
    if year < 1:
        cat_age_month += 15 * month
    elif 1 <=  year < 2:
        cat_age_year += 15 
        cat_age_month = 9 * month
    elif year >= 2:
        cat_age_year += 15 + 9
        
        year -= 2
        
        cat_age_year += year * 4
        
        cat_age_month = month * 4
        
    if cat_age_month > 12:
        cat_age_year += cat_age_month // 12
        cat_age_month = cat_age_month % 12
        
        
    return f"{cat_age_year} {cat_age_month}"
        
        
        
if __name__ == "__main__":
    year, month = map(int, input().split())
    
    print(cats_age(year=year, month=month))