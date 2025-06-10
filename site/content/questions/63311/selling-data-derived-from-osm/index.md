+++
type = "question"
title = "Selling data derived from OSM"
description = '''I&#x27;m considering building and selling a database of drivetime information between various locations in my country, which for boring business-type reasons is something that people in my industry value but aren&#x27;t inclined to generate themselves. It seems like I could, technically speaking, quite easily...'''
date = "2018-05-04T10:59:00Z"
lastmod = "2018-05-04T15:12:00Z"
weight = 63311
keywords = [ "licence", "copyright", "legal" ]
aliases = [ "/questions/63311" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Selling data derived from OSM](/questions/63311/selling-data-derived-from-osm)

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
<span id="post-63311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63311-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-63311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm considering building and selling a database of drivetime information between various locations in my country, which for boring business-type reasons is something that people in my industry value but aren't inclined to generate themselves. It seems like I could, technically speaking, quite easily generate this just from OSM.</p>
<p>It wouldn't contain any map data, just rows like:</p>
<pre><code>{POI x}, {POY y}, {driving distance(x,y)}, {driving time(x,y)}</code></pre>
<p>However I'm not clear on the licencing implications should I do this.</p>
<p><em>Can</em> I legally sell such a database? I'm happy to say "this was calculated with OSM", that's no problem. But I'm not sure if I can commercially licence the results or if it has to be under the ODbL -- and if it <em>is</em> under ODbL, it's not obvious to me if I can sell the database or not.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-licence" rel="tag" title="see questions tagged &#39;licence&#39;">licence</span> <span class="post-tag tag-link-copyright" rel="tag" title="see questions tagged &#39;copyright&#39;">copyright</span> <span class="post-tag tag-link-legal" rel="tag" title="see questions tagged &#39;legal&#39;">legal</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '18, 10:59</strong></p>
<img src="https://secure.gravatar.com/avatar/c89e8e95fbb4f02d4d7ace4ecdc1effe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="paulhunkin&#39;s gravatar image" />
<p><span>paulhunkin</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="paulhunkin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63311" class="comments-container">
&#10;</div>
<div id="comment-tools-63311" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63311-form-container" class="comment-form-container">
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

<span id="63312"></span>

<div id="answer-container-63312" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63312-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-63312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can sell the database thus created, and it has to be licensed under ODbL. This means your clients can use it commercially, but they could also upload it onto a public web page if they so desired. You must not attempt to restrict your clients' freedom to use the data as they see fit. Your clients, in turn, would have to ODbL-license any database they derive from your database.</p>
<p>(For the avoidance of doubt, there is no requirement for you to make your data available for free, but once a client has paid your price, you cannot dictate what they can and cannot do with the data.)</p>
<p>In practice, since the people benefiting from the data being available for free would likely be the competitors of your clients, it is not so likely that your clients will make use of their right to freely disseminate your data. So the business model might work. It would likely work even better if you could sell something customized for the client, which might not even be all that useful to others even if it were published.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '18, 12:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-63312" class="comments-container">
<span id="63313"></span>
<div id="comment-63313" class="comment">
<div id="post-63313-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I understand, that clears up a lot of the questions I had. Thanks! I think you're right, the business model still works. Excellent.</p>
<p>I have a couple of followup questions if you don't mind!</p>
<ul>
<li><p>As I understand it, I don't have to explicitly state <em>before</em> purchase that it's available under ODbL, only include the ODbL in the download and make it clear after purchase. Is that correct? If so, that should dissuade a lot of casual copying.</p></li>
<li><p>An alternative (though more annoying) architecture might be for me to offer this as a SAAS -- so, an API where they can query for "list of drivetimes from PoI-X", for example. In this scenario, does the data returned from the SAAS API come under ODbL too? ie: they can freely distribute that fragment of the full database?</p></li>
</ul>
<p>(My thinking is that that'd make it more annoying for people to distribute a complete copy, as they'd have to assemble it from multiple API requests.)</p>
<p>EDIT: wait, that might fall under "attempting to restrict freedom"...</p>
</div>
<div id="comment-63313-info" class="comment-info">
<span class="comment-age">(04 May '18, 12:54)</span> <span class="comment-user userinfo">paulhunkin</span>
</div>
</div>
<span id="63315"></span>
<div id="comment-63315" class="comment">
<div id="post-63315-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I should point out that it could be argued that the drivetime information itself is a "Produced Work" and as such can be licensed on any terms that fulfil the ODbL attribution requirements.</p>
<p>In such a case the underlying database would have to be provided on request to recipients of the produced work (which however in your scenario is unlikely to happen).</p>
</div>
<div id="comment-63315-info" class="comment-info">
<span class="comment-age">(04 May '18, 14:26)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="63317"></span>
<div id="comment-63317" class="comment">
<div id="post-63317-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a> -- Oh, that's interesting. So to clarify, in the case of a SAAS API, I'd have to let (paying) API users have a full database dump if they ask?</p>
<p>In that case, can I charge additional money for the full database? ie: are my legal obligations covered by <em>preferring</em> people to use the API, but offering a $large-lump-sum-payment copy of the database for users to buy if they wish.</p>
<p>Even if they can then legally host the copy for free, I'd be ok with that, really -- practically speaking it'd be quite unlikely to happen.</p>
<p>(this is surprisingly complicated!)</p>
</div>
<div id="comment-63317-info" class="comment-info">
<span class="comment-age">(04 May '18, 14:38)</span> <span class="comment-user userinfo">paulhunkin</span>
</div>
</div>
<span id="63318"></span>
<div id="comment-63318" class="comment">
<div id="post-63318-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually it is not really complicated, the edge cases are sometime a bit fuzzy.</p>
<p>The ODBL distinguishes between the database and derivatives that are databases and those that are not, for example: maps.</p>
<p>A SAAS delivering a single result is likely the later.</p>
</div>
<div id="comment-63318-info" class="comment-info">
<span class="comment-age">(04 May '18, 15:12)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63312" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63312-form-container" class="comment-form-container">
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

