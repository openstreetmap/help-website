+++
type = "question"
title = "Onetime bulk reverse geocoding: which amout is okay?"
description = '''Hello, In a project I currently working for there&#x27;s a need of reverse geocoding of ~15 000 - 20 000 latitude and longitude coordinates. To be more specific I&#x27;m not interested in exact street address but just in administrative entities for these coordinates, cities or towns maximum. Nominatim usage p...'''
date = "2014-01-22T06:17:00Z"
lastmod = "2016-09-24T10:49:00Z"
weight = 30056
keywords = [ "bulk", "reversegeocoding", "geocoding", "nominatim" ]
aliases = [ "/questions/30056" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Onetime bulk reverse geocoding: which amout is okay?](/questions/30056/onetime-bulk-reverse-geocoding-which-amout-is-okay)

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
<span id="post-30056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30056-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>In a project I currently working for there's a need of reverse geocoding of ~15 000 - 20 000 latitude and longitude coordinates. To be more specific I'm not interested in exact street address but just in administrative entities for these coordinates, cities or towns maximum.</p>
<p>Nominatim usage policy doesn't encourage bulk geocoding and amount of my requests is quite large but I have a very simple single-threaded script to do it which seems to fall under the limitations of usage policies. The speed is not critical and setting up local Nominatim server is quite an overkill for this task. Unfortunately even business geocoding solution are aimed more for regular application use while I'm in fact interested in the data itself.</p>
<p>So there're my main questions:</p>
<ol>
<li>Is it possible to reverse geocode about ~20000 using public API. If not then what amount of requests is acceptable under usage policies?</li>
<li>If it is, should I force something like 1 second wait intervals between requests to ensure lower load on public servers.</li>
<li>Should I notify about my bulk geocoding</li>
</ol>
<p>Sorry if there're somewhere <em>exactly</em> the same questions I couldn't found one</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bulk" rel="tag" title="see questions tagged &#39;bulk&#39;">bulk</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '14, 06:17</strong></p>
<img src="https://secure.gravatar.com/avatar/26df8ab333942090a045ff20f28d5cb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seqai&#39;s gravatar image" />
<p><span>seqai</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seqai has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jan '14, 12:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-30056" class="comments-container">
<span id="52212"></span>
<div id="comment-52212" class="comment">
<div id="post-52212-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For info I converted an extra "answer" here to a question. It is now at <a href="https://help.openstreetmap.org/questions/52210/interested-in-building-a-bulk-geocoder-app-that-could-be-used-locally-in-the-browse">https://help.openstreetmap.org/questions/52210/interested-in-building-a-bulk-geocoder-app-that-could-be-used-locally-in-the-browse</a> .</p>
</div>
<div id="comment-52212-info" class="comment-info">
<span class="comment-age">(24 Sep '16, 10:49)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30056" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30056-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="30060"></span>

<div id="answer-container-30060" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30060-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-30060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="seqai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="http://wiki.openstreetmap.org/wiki/Nominatim_usage_policy">Nominatim Usage Policy</a> for OSM's own Nominatim instance says</p>
<blockquote>
<p>As a general rule, bulk geocoding of larger amounts of data is not encouraged. If you have regular geocoding tasks, please, look into alternatives below. Smaller one-time bulk tasks may be permissible, if these additional rules are followed</p>
<ul>
<li><p>limit your requests to a single thread</p></li>
<li><p>limited to 1 machine only, no distributed scripts (including multiple Amazon EC2 instances or similar)</p></li>
<li><p>Results must be cached on your side. Clients sending repeatedly the same query may be classified as faulty and blocked.</p></li>
</ul>
</blockquote>
<p>If you say that speed is not critical for you, then to be absolutely safe I'd insert a longer pause between requests - say, 5 seconds - which would take your total run time to about 1.5 days, and you could be sure not to tax OSM's servers too much.</p>
<p>You could also look into <a href="http://developer.mapquest.com/web/products/open/nominatim">MapQuest's Nominatim Server</a> the usage policy of which is somewhat more relaxed than OpenStreetMap's (they have bigger machines).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '14, 06:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jan '14, 06:48</strong> </span></p>
</div>
</div>
<div id="comments-container-30060" class="comments-container">
<span id="30062"></span>
<div id="comment-30062" class="comment">
<div id="post-30062-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think that currently it's the best solution for me. If constant requests for almost 2 days is not a problem then I think I'll go for it. The script is really tiny and I can use it even on my ancient notebook running it for couple of days. From MapQuest usage policies I understood that they're more oriented towards software and web-developers so I'm not sure that onetime bulk geocoding falls under it. Thank you very much!</p>
</div>
<div id="comment-30062-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 07:02)</span> <span class="comment-user userinfo">seqai</span>
</div>
</div>
<span id="30070"></span>
<div id="comment-30070" class="comment">
<div id="post-30070-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@seqai</span>: By the way: <a href="/questions/30066/nominatim-doesnt-respond-as-of-22-1-2014-0814-cet">Today there seem to be problems</a> with the osm.org Nominatim server, so I suggest not to start today. <a href="http://munin.openstreetmap.org/openstreetmap/poldi.openstreetmap/index.html#nominatim">Here are the stats</a> if you want to look for low load times or problems.</p>
</div>
<div id="comment-30070-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 12:16)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="30071"></span>
<div id="comment-30071" class="comment">
<div id="post-30071-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@seqai</span>: Oh, and since you say that you have a simple script: take care to set a proper user agent (maybe your email address or a reference to this question here?). This is mentioned in the "requirements" on the policy page which also mentions one request per second as maximum.</p>
</div>
<div id="comment-30071-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 12:24)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="30074"></span>
<div id="comment-30074" class="comment">
<div id="post-30074-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@aseerel4c26</span> Thank you for notifying about the problems, though I've already had my script running and loaded 1510 coordinates with 5 sec pause between requests and haven't met any problems. I've included this exact information ou mentioned (email and link to this question as it's requested in policies) in the User-agent. For now I'm going to pause to wait until everything is ok.</p>
</div>
<div id="comment-30074-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 12:43)</span> <span class="comment-user userinfo">seqai</span>
</div>
</div>
</div>
<div id="comment-tools-30060" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30060-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30061"></span>

<div id="answer-container-30061" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30061-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30061-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-30061-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To get which country and city some coordinate is in, you can use <a href="http://wiki.osm.org/wiki/Overpass_API">Overpass API</a>. Please see this <a href="http://overpass-turbo.eu/s/2bM">the example</a>. You can start it with the button "Execute".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '14, 06:52</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-30061" class="comments-container">
&#10;</div>
<div id="comment-tools-30061" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30061-form-container" class="comment-form-container">
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

