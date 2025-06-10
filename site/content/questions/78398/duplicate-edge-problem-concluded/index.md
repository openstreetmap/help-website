+++
type = "question"
title = "Duplicate Edge problem [Concluded]"
description = '''There&#x27;s &#x27;Duplicate edge&#x27; which is easily resolved by e.g. separating a street from the edge of a square and then there are &#x27;duplicate edge&#x27; where a e.g. complex pedestrian area is drawn, one part tagged with a cobblestone pattern, another part tagged as marble covered etc. Another simpler example a ...'''
date = "2021-01-18T15:17:00Z"
lastmod = "2021-01-18T18:46:00Z"
weight = 78398
keywords = [ "duplicate", "edge" ]
aliases = [ "/questions/78398" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate Edge problem \[Concluded\]](/questions/78398/duplicate-edge-problem-concluded)

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
<span id="post-78398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78398-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There's 'Duplicate edge' which is easily resolved by e.g. separating a street from the edge of a square and then there are 'duplicate edge' where a e.g. complex pedestrian area is drawn, one part tagged with a cobblestone pattern, another part tagged as marble covered etc. Another simpler example a pedestrian area, bout 4 meters wide, 150 long joins a square <a href="https://www.openstreetmap.org/way/702458985">https://www.openstreetmap.org/way/702458985</a> . The joining edge is marked as duplicate. It makes no sense to me why 2 in effect basically identical areas cant be sharing edges/nodes. Bar artificially separating them then create a single connect node 'to map around', no solution (and the facepalms are up to be slapped).</p>
<p>Ref: wiki <a href="https://wiki.openstreetmap.org/wiki/Key:area:highway">https://wiki.openstreetmap.org/wiki/Key:area:highway</a></p>
<p>BTW, see these areas also often being thrown out as "no feature tag ways".</p>
<p>Any ideas to resolve these with a note that 'not mapping them details is not an option'. OsmAnd e.g. maps some of these properly like the area:highway=motorway areas.</p>
<p>cheers</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-edge" rel="tag" title="see questions tagged &#39;edge&#39;">edge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jan '21, 15:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ed39ace8cbefe3b5c45da98f60f5e34c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SekeRob&#39;s gravatar image" />
<p><span>SekeRob</span><br />
<span class="score" title="211 reputation points">211</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SekeRob has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jan '21, 18:47</strong> </span></p>
</div>
</div>
<div id="comments-container-78398" class="comments-container">
<span id="78401"></span>
<div id="comment-78401" class="comment">
<div id="post-78401-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Where are you seeing "duplicate edge" reported as a problem? From the way you describe it, it sounds like usually it is a warning that should be ignored.</p>
</div>
<div id="comment-78401-info" class="comment-info">
<span class="comment-age">(18 Jan '21, 16:00)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="78404"></span>
<div id="comment-78404" class="comment">
<div id="post-78404-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's a link on the Neis report, under the sub topic of 'routing' Your page: <a href="https://hdyc.neis-one.org/?EdLoach.">https://hdyc.neis-one.org/?EdLoach.</a> These 'Duplicate Edge' are classed as geometry.</p>
<p>Been working me bud off to get all those for routing and QA error metric types below 25, just this one and a few more mostly give me the famous 3rd finger. If ignorable, I'll be happy to add these items that are legally 'ignored' to my vertical archive list. Is there some master/cheat list for those?</p>
<p>thanks for responding.</p>
</div>
<div id="comment-78404-info" class="comment-info">
<span class="comment-age">(18 Jan '21, 17:15)</span> <span class="comment-user userinfo">SekeRob</span>
</div>
</div>
<span id="78405"></span>
<div id="comment-78405" class="comment">
<div id="post-78405-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8468/sekerob">@SekeRob</a> That's an OSMI error - and I'd agree that it can usually be ignored. I know it's tempting to try and whittle down those OSMI and Osmose errors, but some of those "errors" are badly implemented and/or not actually errors. Don't think of it as a scorecard - no one else is keeping score or judging your mapping based on those errors! (or at least no one SHOULD be)</p>
</div>
<div id="comment-78405-info" class="comment-info">
<span class="comment-age">(18 Jan '21, 18:29)</span> <span class="comment-user userinfo">GregRetro</span>
</div>
</div>
<span id="78406"></span>
<div id="comment-78406" class="comment">
<div id="post-78406-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, I'll make my personal list of items to ignore, some like 'island car' truly mind boggling in instances. If using the OSM build-in navigator at least, it's impossible to navigate at times to get somewhere but walk the last mile. Using it at times to find the join where things hang up.</p>
<p>Have a good evening.</p>
</div>
<div id="comment-78406-info" class="comment-info">
<span class="comment-age">(18 Jan '21, 18:46)</span> <span class="comment-user userinfo">SekeRob</span>
</div>
</div>
</div>
<div id="comment-tools-78398" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78398-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

