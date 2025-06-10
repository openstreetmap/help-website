+++
type = "question"
title = "OverpassAPI: queries fail randomly"
description = '''Hello, I have been trying to query OSM data using overpass-api.de but it&#x27;s working pretty randomly. For example, It gets data twice in a row, but the third request timeouts, or works once then fails two or three times, etc. I haven&#x27;t been able to determine any patterns in this. it just seems to fail...'''
date = "2019-08-16T16:53:00Z"
lastmod = "2019-08-19T17:07:00Z"
weight = 70402
keywords = [ "query", "random", "request", "timeout", "failed" ]
aliases = [ "/questions/70402" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OverpassAPI: queries fail randomly](/questions/70402/overpassapi-queries-fail-randomly)

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
<span id="post-70402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70402-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have been trying to query OSM data using overpass-api.de but it's working pretty randomly. For example, It gets data twice in a row, but the third request timeouts, or works once then fails two or three times, etc. I haven't been able to determine any patterns in this. it just seems to fail at random times.</p>
<p>I am getting Connection Timeout as a result of a failed request. Have in mind that It's the same code that sends the request. Same requests work and fail randomly.</p>
<p>Is there anything I might be missing in here? Do You have any idea what could cause this?</p>
<p>EDIT: Thanks for the suggestion! Query example: [bbox:-4.8829942,29.6411133,-4.8720477,29.6520996][timeout:40]; ( node["building"]; node[~".<em>"~"^building$"]; way["building"]; way[~".</em>"~"^building$"]; relation["building"]; relation[~".*"~"^building$"]; ); out meta;&gt;;out meta;</p>
<p>Thanks, Filip</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-random" rel="tag" title="see questions tagged &#39;random&#39;">random</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-timeout" rel="tag" title="see questions tagged &#39;timeout&#39;">timeout</span> <span class="post-tag tag-link-failed" rel="tag" title="see questions tagged &#39;failed&#39;">failed</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '19, 16:53</strong></p>
<img src="https://secure.gravatar.com/avatar/88a063b5119006eb5b95951959bdd2f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fica&#39;s gravatar image" />
<p><span>fica</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fica has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Aug '19, 18:38</strong> </span></p>
</div>
</div>
<div id="comments-container-70402" class="comments-container">
<span id="70403"></span>
<div id="comment-70403" class="comment">
<div id="post-70403-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi Fica, could you please edit your question with the query in question? Then we can give feedback. In general, any request randomly can have to wait because of too much data to return or just because it's busy on the server.</p>
</div>
<div id="comment-70403-info" class="comment-info">
<span class="comment-age">(16 Aug '19, 18:16)</span> <span class="comment-user userinfo">tijmenheid</span>
</div>
</div>
<span id="70404"></span>
<div id="comment-70404" class="comment">
<div id="post-70404-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi tijamenheid,</p>
<p>Thanks for the quick reply! I included a query example. Have in mind that this exact query, for example, works every second time or something like that.</p>
</div>
<div id="comment-70404-info" class="comment-info">
<span class="comment-age">(16 Aug '19, 18:41)</span> <span class="comment-user userinfo">fica</span>
</div>
</div>
<span id="70413"></span>
<div id="comment-70413" class="comment">
<div id="post-70413-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could you clarify what data is being returned "twice"?</p>
<p>To simplify use the 'nwr' option [bbox:-4.8829942,29.6411133,-4.8720477,29.6520996][timeout:40]; nwr[building]; (._;&gt;;); out meta;</p>
<p>This returns 1949 polygons, the same as your routine.</p>
<p>This line - nwr[~".*"~"^building$"]; is looking for tags with the value of 'building' &amp; in your example returns nothing</p>
</div>
<div id="comment-70413-info" class="comment-info">
<span class="comment-age">(18 Aug '19, 17:19)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="70421"></span>
<div id="comment-70421" class="comment">
<div id="post-70421-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi DaveF,</p>
<p>I don't have much experience with the query language so this was how I queried parts of polygons that were partially out of the bounding box. I also wanted to query tags by value as well, just to be sure not to miss anything. Thank You for the suggestion.</p>
<p>Today queries seem to work fine, none resulted in a timeout. It was probably an overload on the server since I ran the same queries as I did before.</p>
</div>
<div id="comment-70421-info" class="comment-info">
<span class="comment-age">(19 Aug '19, 11:43)</span> <span class="comment-user userinfo">fica</span>
</div>
</div>
<span id="70425"></span>
<div id="comment-70425" class="comment">
<div id="post-70425-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The Default timeout value is 180. Setting it to 40 means the routine will quit earlier.</p>
</div>
<div id="comment-70425-info" class="comment-info">
<span class="comment-age">(19 Aug '19, 17:07)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-70402" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70402-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

