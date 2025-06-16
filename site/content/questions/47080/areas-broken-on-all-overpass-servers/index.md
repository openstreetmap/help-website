+++
type = "question"
title = "Areas broken on all overpass servers?"
description = '''Ed Loach´s &quot;Admin Boundary Analysis&quot; service has not updated since 15 November. I contacted Ed about this and he says it´s being crippled at the moment by the &quot;area update&quot; issues in Overpass. According to the Platform Status page, all three overpass instances (France, Germany, Russia) seem to be ha...'''
date = "2015-12-09T18:56:00Z"
lastmod = "2015-12-22T10:50:00Z"
weight = 47080
keywords = [ "overpass" ]
aliases = [ "/questions/47080" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Areas broken on all overpass servers?](/questions/47080/areas-broken-on-all-overpass-servers)

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
<span id="post-47080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47080-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Ed Loach´s "Admin Boundary Analysis" service has not updated since 15 November. I contacted Ed about this and he says it´s being crippled at the moment by the "area update" issues in Overpass.</p>
<p>According to the Platform Status page, all three overpass instances (France, Germany, Russia) seem to be having the same problem with updating areas.</p>
<p>Does anyone know what is going on? Will this be fixed soon? Or will the change that caused the problem be backed out?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Dec '15, 18:56</strong></p>
<img src="https://secure.gravatar.com/avatar/81868786ff539d9a5b1f21ed57b6e13a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="csmale&#39;s gravatar image" />
<p><span>csmale</span><br />
<span class="score" title="81 reputation points">81</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="csmale has one accepted answer">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Dec '15, 10:32</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-47080" class="comments-container">
<span id="47089"></span>
<div id="comment-47089" class="comment">
<div id="post-47089-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>As an aside, I used to download a geofabrik extract daily, then filter to just the boundary related stuff, but Overpass proved more efficient. I should perhaps switch to using a local database and processing the daily diff files, but haven't got around to it.</p>
</div>
<div id="comment-47089-info" class="comment-info">
<span class="comment-age">(10 Dec '15, 13:12)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="47102"></span>
<div id="comment-47102" class="comment">
<div id="post-47102-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Platform status has been updated to suggest the German instance is OK now. I am still getting the same Gateway Timeout I've been getting since it last worked: wget -Ogreat_britain.osm "http://overpass-api.de/api/interpreter?data=[timeout:86400];(rel<a href="50.06419,-11.1621,59.04055,2.19727">"boundary"</a>;);( .<em>;way(r););out meta;" --2015-12-11 16:04:17-- <a href="http://overpass-api.de/api/interpreter?data=%5Btimeout:86400%5D;(rel">http://overpass-api.de/api/interpreter?data=[timeout:86400];(rel</a><a href="50.06419,-11.1621,59.04055,2.19727">boundary</a>;);(%20.</em>;way(r););out%20 meta; Resolving overpass-api.de... 46.4.41.83 Connecting to overpass-api.de|46.4.41.83|:80... connected. HTTP request sent, awaiting response... 504 Gateway Timeout 2015-12-11 16:04:33 ERROR 504: Gateway Timeout.</p>
</div>
<div id="comment-47102-info" class="comment-info">
<span class="comment-age">(11 Dec '15, 16:10)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47080-form-container" class="comment-form-container">
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

<span id="47105"></span>

<div id="answer-container-47105" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47105-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The issue <a href="https://help.openstreetmap.org/users/339/edloach"></a><a href="https://help.openstreetmap.org/users/339/edloach">@EdLoach</a></a> is facing is pretty much unrelated to the <em>area update</em> issue. In fact his query doesn't even use the word <code>area</code> in there, so there's nothing to worry about. It would have worked all the time.</p>
<p>Now, the reason for the 504 Gateway issue is the <em>way</em> too large timeout value. I'd suggest to reduce that at least down to 3600 seconds or even lower. 24hours timeout is deemed to be a resource killer by Overpass API and the query get immediately canceled.</p>
<p>Here's my log for the same query with 3600 seconds timeout - results returned back in 1 minute 30 seconds.</p>
<pre><code>wget &quot;http://overpass-api.de/api/interpreter?data=[timeout:3600];(rel[&quot;boundary&quot;](50.06419,-11.1621,59.04055,2.19727););( ._;way(r););out meta;&quot; -O res.osm
--2015-12-11 17:11:28--  http://overpass-api.de/api/interpreter?data=[timeout:3600];(rel[boundary](50.06419,-11.1621,59.04055,2.19727););(%20._;way(r););out%20meta;
Resolving overpass-api.de (overpass-api.de)... 2a01:4f8:131:6109::2, 46.4.41.83
Connecting to overpass-api.de (overpass-api.de)|2a01:4f8:131:6109::2|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [application/osm3s+xml]
Saving to: &#39;res.osm&#39;
&#10;    [                              &lt;=&gt;                                             ] 326,493,532 28.3MB/s   in 8.3s
&#10;2015-12-11 17:12:52 (37.6 MB/s) - &#39;res.osm&#39; saved [326493532]</code></pre>
<p>NB: The issue on the French server was reported some time back but I don't have an up to date status from <a href="https://help.openstreetmap.org/users/3436/sly">@sly</a>. The Russian server is facing some hard disk issues now and then. The issue on the German server was reported back in November, but I also don't have a feedback from Roland, why the update job stopped. Nevertheless, the area creation job was scheduled again on overpass-api.de, so you should get up-to-date areas now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Dec '15, 17:17</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Dec '15, 18:09</strong> </span></p>
</div>
</div>
<div id="comments-container-47105" class="comments-container">
<span id="47117"></span>
<div id="comment-47117" class="comment">
<div id="post-47117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! Scheduled task updated and due to run in less than an hour from now. I presume I got 86400 from some example query somewhere and as noted above it was working...</p>
</div>
<div id="comment-47117-info" class="comment-info">
<span class="comment-age">(12 Dec '15, 09:33)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="47263"></span>
<div id="comment-47263" class="comment">
<div id="post-47263-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Area creation on overpass-api.de seems to have stopped again 4 days ago (see the yellow background in overpass turbo on the bottom right for queries involving areas).</p>
<p>Unfortunately I don't have any more details. Roland is the only person having access to production, afaik.</p>
</div>
<div id="comment-47263-info" class="comment-info">
<span class="comment-age">(22 Dec '15, 10:50)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-47105" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47105-form-container" class="comment-form-container">
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

