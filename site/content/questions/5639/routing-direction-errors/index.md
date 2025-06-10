+++
type = "question"
title = "Routing / Direction Errors"
description = '''Hi While in driving mode and following directions/route on NavDroyd I found several instances where there were errors e.g. a request to turn right where there was a NO Turn Right sign  a roundabout showing 5 exits when 1 of those was a pedestrian entrance to a church grounds and blocked to vehicles ...'''
date = "2011-06-08T18:45:00Z"
lastmod = "2011-06-08T20:39:00Z"
weight = 5639
keywords = [ "routing", "error" ]
aliases = [ "/questions/5639" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Routing / Direction Errors](/questions/5639/routing-direction-errors)

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
<span id="post-5639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5639-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>While in driving mode and following directions/route on NavDroyd I found several instances where there were errors</p>
<p>e.g. a request to turn right where there was a NO Turn Right sign a roundabout showing 5 exits when 1 of those was a pedestrian entrance to a church grounds and blocked to vehicles being routed up an exit slip road thru' traffic lights and back onto an entrance slip road to a motorway instead of being roted thru' on the motorway.</p>
<p>I registered with OSM to edit/correct/notify the bugs but I'm totally new to OSM (though very experienced in computers, PCs, PC software and GUIs) but was unable to find options to make the corrections for the errors noted above.</p>
<p>How can I edit or report these errors?</p>
<p>Tom H</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '11, 18:45</strong></p>
<img src="https://secure.gravatar.com/avatar/26776703fd97668c6b87d59971e59e55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="than103&#39;s gravatar image" />
<p><span>than103</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="than103 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jun '11, 20:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span></p>
</div>
</div>
<div id="comments-container-5639" class="comments-container">
&#10;</div>
<div id="comment-tools-5639" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5639-form-container" class="comment-form-container">
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

<span id="5640"></span>

<div id="answer-container-5640" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5640-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-5640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>By far and away the easiest way to mark/notify errors is to use <a href="http://wiki.openstreetmap.org/wiki/OpenStreetBugs">OpenStreetBugs</a> to mark where the error occur. How fast they are fixed will depend on how active mappers are in the local area. OpenStreetBugs is not yet integrated into the core functionality of OSM, so bugs are not immediately obvious to mappers.</p>
<p>Some of the problems you describe: turn restrictions, in particular, can be recognised as an 'advanced mapping technique'. This means that a certain familiarity with the basic mechanics of OSM objects and editors is needed to make such changes with confidence. For instance a typical NO RIGHT TURN requires that the way one is turning from is split at the junction point. Then the junction point ('via') the road one is turning 'from' and the road one is trying to turn in'to' are added to a <a href="http://wiki.openstreetmap.org/wiki/Turn_restrictions">turn restriction</a> <a href="http://wiki.openstreetmap.org/wiki/Relations">relation</a> with the named roles. As one can see from this description its currently hard to describe this without a fair bit of OSM-specific terminology. Here is <a href="http://www.openstreetmap.org/browse/relation/1026935">an example</a> from my local area.</p>
<p>Additionally, it is useful to check that the errors genuinely exist in OSM and are not due to a partial parsing of OSM data by the application. For instance several routers ignored <code>barrier=*</code> tags and routed through bollards, gates etc. Another common problem with router data is that it is out-of-date and the routing problems encountered have already been fixed. A good approach is to try the route in one of the on-line routing providers (e.g., <a href="http://maps.cloudmade.com/">Cloudmade</a>, <a href="http://openrouteservice.org/">OpenRouteService</a>, <a href="http://open.mapquest.com/">Open MapQuest</a>, <a href="http://www.yournavigation.org/">Your Navigation</a>) to see if the problem is still current. Open MapQuest is usually only minutes behind the main OSM database.</p>
<p>For detailed assistance with your specific issues, you can ask on the IRC channels, the Forum, or a local mailing list. The general #OSM channel on IRC is likely to be the most responsive, particularly if you can provide a permalink to the area in question.</p>
<p>We know that turn restrictions are not particularly well mapped. For instance I analysed <a href="http://www.flickr.com/photos/sk53_osm/5426090158/">the distribution</a> of turn restrictions in Great Britain earlier in the year and many administrative districts did not have any mapped at all. So we really welcome information and contributions which can improve the OSM data in this respect.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '11, 19:27</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-5640" class="comments-container">
<span id="5641"></span>
<div id="comment-5641" class="comment">
<div id="post-5641-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... and further you have to investigate whether the OSM data contains already the necessary turn restrictions or similar routing relevant rules AND whether the navigating program (like NavDroyd) pays attention to that rules.</p>
</div>
<div id="comment-5641-info" class="comment-info">
<span class="comment-age">(08 Jun '11, 20:39)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-5640" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5640-form-container" class="comment-form-container">
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

