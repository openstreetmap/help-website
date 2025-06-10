+++
type = "question"
title = "How to handle python djangon geocoder osm error if user enter invalid city name"
description = '''Did anyone know how to handle python geocoder osm error if user enter invalid city name? I am using it in Django. When user input valid city name it saving to my database and showing on map but I can&#x27;t stop user to put invalid city name and prevent saving to my database. here is part of my code: def...'''
date = "2021-04-08T16:07:00Z"
lastmod = "2021-04-09T08:35:00Z"
weight = 79569
keywords = [ "geocoding", "reversegeocoding", "osm", "geodjango" ]
aliases = [ "/questions/79569" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to handle python djangon geocoder osm error if user enter invalid city name](/questions/79569/how-to-handle-python-djangon-geocoder-osm-error-if-user-enter-invalid-city-name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79569-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Did anyone know how to handle python geocoder osm error if user enter invalid city name? I am using it in Django. When user input valid city name it saving to my database and showing on map but I can't stop user to put invalid city name and prevent saving to my database. here is part of my code:</p>
<pre><code>def Distance_view(request):
    if request.method == &#39;POST&#39;:
        form = Search(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Search()
&#10;
    address = FindDistance.objects.all().last()
    location = geocoder.osm(address)</code></pre>
<p>right now if user give valid address then it showing on map but if user give wrong address it's saving to my database and raise this error. After deleting the wrong address from my database it's start working. How to prevent user to give wrong address and prevent saving to my database.</p>
<pre><code>&quot;ValueError at /map
&#10;Location should consist of two numerical values, but None of type &lt;class &#39;NoneType&#39;&gt; is not convertible to float.&quot;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-geodjango" rel="tag" title="see questions tagged &#39;geodjango&#39;">geodjango</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '21, 16:07</strong></p>
<img src="https://secure.gravatar.com/avatar/28eb2f1e469f0b4e62abdc1e5697cf19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tusar25&#39;s gravatar image" />
<p><span>tusar25</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tusar25 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Apr '21, 16:09</strong> </span></p>
</div>
</div>
<div id="comments-container-79569" class="comments-container">
&#10;</div>
<div id="comment-tools-79569" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79569-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="79577"></span>

<div id="answer-container-79577" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79577-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You would have to check that your location variable has the right type of data before saving it to a database. As your geocoder probably uses nominatim, it would return an empty result if the city name entered can't be found.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '21, 08:35</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-79577" class="comments-container">
&#10;</div>
<div id="comment-tools-79577" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79577-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

