+++
type = "question"
title = "Overpass returns empty dataset on phone."
description = '''I posted this yesterday, but as I don&#x27;t see it show up I&#x27;ll try again: When I use https://overpass-turbo.eu/ on my phone in a webbrowser (Motorola, android 9, firefox chrome) it says &quot;map intentionally left blank (received empty dataset)&quot;. If I run exactly the same query on the same area on my lapto...'''
date = "2023-05-15T13:33:00Z"
lastmod = "2023-05-17T09:07:00Z"
weight = 87262
keywords = [ "overpass-turbo" ]
aliases = [ "/questions/87262" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass returns empty dataset on phone.](/questions/87262/overpass-returns-empty-dataset-on-phone)

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
<span id="post-87262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87262-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I posted this yesterday, but as I don't see it show up I'll try again:</p>
<p>When I use <a href="https://overpass-turbo.eu/">https://overpass-turbo.eu/</a> on my phone in a webbrowser (Motorola, android 9, firefox chrome) it says "map intentionally left blank (received empty dataset)". If I run exactly the same query on the same area on my laptop it does return a dataset. I tried different queries in different browsers and for different areas but the problem persists.</p>
<p>What can this be? How can I fix this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 May '23, 13:33</strong></p>
<img src="https://secure.gravatar.com/avatar/dc4f39963aa53a2e8b65e6bdd992ee5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Silent&#39;s gravatar image" />
<p><span>Silent</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Silent has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87262" class="comments-container">
<span id="87263"></span>
<div id="comment-87263" class="comment">
<div id="post-87263-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Open overpass turbo on your device with the desired query. Go to export -&gt; raw data directly from Overpass API. Save the result and take a look at it. Does it contain any error message? Or is it really empty?</p>
</div>
<div id="comment-87263-info" class="comment-info">
<span class="comment-age">(15 May '23, 14:11)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="87264"></span>
<div id="comment-87264" class="comment">
<div id="post-87264-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Maybe you can share your query? It works for me with <a href="https://overpass-turbo.eu/s/1uYS">this one</a>, on Motorola, Android 9 and Firefox. ;-)</p>
</div>
<div id="comment-87264-info" class="comment-info">
<span class="comment-age">(15 May '23, 15:19)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="87265"></span>
<div id="comment-87265" class="comment">
<div id="post-87265-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to add to this, I regularly create queries on desktop, and share them with myself by email fro later use on mobile. I've not seen a problem yet...</p>
</div>
<div id="comment-87265-info" class="comment-info">
<span class="comment-age">(15 May '23, 16:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="87268"></span>
<div id="comment-87268" class="comment">
<div id="post-87268-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the replies so far.</p>
<blockquote>
<p>export -&gt; raw data directly from Overpass API</p>
</blockquote>
<p>No error is shown, just the usual header and then an empty elements. Full text of the returned raw data:</p>
<p>{ "version": 0.6, "generator": "Overpass API 0.7.60.2 e4cf9f7a", "osm3s": { "timestamp_osm_base": "2023-05-15T16:08:09Z", "copyright": "The data included in this document is from www.openstreetmap.org. The data is made available under ODbL." }, "elements": [</p>
<p>] }</p>
</div>
<div id="comment-87268-info" class="comment-info">
<span class="comment-age">(15 May '23, 17:28)</span> <span class="comment-user userinfo">Silent</span>
</div>
</div>
<span id="87269"></span>
<div id="comment-87269" class="comment not_top_scorer">
<div id="post-87269-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>Maybe you can share your query?</p>
</blockquote>
<p>Sure, but intuitively I'ld say it's not the query as I tried different queries and for each exactly the same query works on my laptop, but not on my phone. One example query is:</p>
<p>/ <em>This has been generated by the overpass-turbo wizard. The original search was: “shop = bicycle”</em> / [out:json][timeout:25]; // gather results ( // query part for: “shop=bicycle” node<a href="%7B%7Bbbox%7D%7D">"shop"="bicycle"</a>; way<a href="%7B%7Bbbox%7D%7D">"shop"="bicycle"</a>; relation<a href="%7B%7Bbbox%7D%7D">"shop"="bicycle"</a>; ); // print results out body;</p>
<blockquote>
<p>; out skel qt;</p>
</blockquote>
<p>Typing this made me think that maybe the issue is that the bound box fails to define. But makes no difference, works on laptop but not on phone. Code used:</p>
<p>/ <em>This has been generated by the overpass-turbo wizard. The original search was: “shop = bicycle in Eindhoven”</em> / [out:json][timeout:25]; // fetch area “Eindhoven” to search in {{geocodeArea:Eindhoven}}-&gt;.searchArea; // gather results ( // query part for: “shop=bicycle” node<a href="area.searchArea">"shop"="bicycle"</a>; way<a href="area.searchArea">"shop"="bicycle"</a>; relation<a href="area.searchArea">"shop"="bicycle"</a>; ); // print results out body;</p>
<blockquote>
<p>; out skel qt;</p>
</blockquote>
</div>
<div id="comment-87269-info" class="comment-info">
<span class="comment-age">(15 May '23, 17:34)</span> <span class="comment-user userinfo">Silent</span>
</div>
</div>
<span id="87271"></span>
<div id="comment-87271" class="comment not_top_scorer">
<div id="post-87271-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately parts of your query aren't visible due to bad formatting. It might be better to share a link to it instead (via the share button at overpass-turbo).</p>
</div>
<div id="comment-87271-info" class="comment-info">
<span class="comment-age">(16 May '23, 06:58)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="87274"></span>
<div id="comment-87274" class="comment">
<div id="post-87274-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://overpass-turbo.eu/s/1v3W">https://overpass-turbo.eu/s/1v3W</a></p>
</div>
<div id="comment-87274-info" class="comment-info">
<span class="comment-age">(17 May '23, 09:01)</span> <span class="comment-user userinfo">Silent</span>
</div>
</div>
<span id="87275"></span>
<div id="comment-87275" class="comment not_top_scorer">
<div id="post-87275-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Works on my phone, the results are displayed after tapping run (Firefox 113, Android 10).</p>
</div>
<div id="comment-87275-info" class="comment-info">
<span class="comment-age">(17 May '23, 09:07)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-87262" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-87262-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

