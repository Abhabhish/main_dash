if ratio == 'ethnicity_wise_gender':
        data = RecordingDetail.objects.values('ethnicity').annotate(
            male_count=Count(Case(When(gender='M', then=1))),
            female_count=Count(Case(When(gender='F', then=1)))
        ).order_by('ethnicity')
        
        res = {
            'm': [],
            'f': [],
        }
        
        for item in data:
            res['m'].append(item['male_count'])
            res['f'].append(item['female_count'])
        return JsonResponse(res)