+++
type = "question"
title = "How to make a map showing &quot;All of (tag)&quot;?"
description = '''Hi - Newbie needs guidance. A few of us in the Boston tech startup community want to create a map showing the location of all the tech companies in Boston. OSM and tagging appear to be well-suited to this, but as a newbie I don&#x27;t know where to start. Here are the things I know we want as an outcome:...'''
date = "2013-08-16T04:12:00Z"
lastmod = "2013-08-21T16:51:00Z"
weight = 25467
keywords = [ "tagging" ]
aliases = [ "/questions/25467" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to make a map showing "All of (tag)"?](/questions/25467/how-to-make-a-map-showing-all-of-tag)

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
<span id="post-25467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25467-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-25467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi -</p>
<p>Newbie needs guidance.</p>
<p>A few of us in the Boston tech startup community want to create a map showing the location of all the tech companies in Boston. OSM and tagging appear to be well-suited to this, but as a newbie I don't know where to start.</p>
<p>Here are the things I know we want as an outcome:</p>
<ul>
<li>Normal, zoomable map</li>
<li>Companies are shown just as an Office would be, but are particularly tagged to be a tech company. (See below for defining what that means.)</li>
<li>There is a view of the map showing only these tagged nodes (e.g. doesn't show other tagged elements like amenities, etc.)</li>
<li>This is on the public OSM (i.e. not a locally-installed version of OSM)</li>
<li>Community-maintained. All the people in a local Tech ecosystem would keep the tagged offices up-to-date over time.</li>
</ul>
<p>It's not clear to me how to approach this tagging, since "technology office / company" isn't in the tag database, and I don't know if / how user-defined tags work. I assert that people in many cities / areas in the world may want to have a similar "map of all the tech companies in my town," so this might be a generally-useful tag to add in OSM's tag structure. (I suspect there will be more tech company employees adding such nodes to OSM than, say "(real) estate" companies (for which there is a tag). ;-)</p>
<p>Note: I realize there's some ambiguity in what constitutes a "technology company." We can create some guidelines in this question thread, or (maybe better) in a separate discussion thread in the OSM Forum.</p>
<p>Can somebody help get me started?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '13, 04:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ddb1bbd9eaf3b5b37477320f591d3b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jay%20Batson&#39;s gravatar image" />
<p><span>Jay Batson</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jay Batson has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25467" class="comments-container">
&#10;</div>
<div id="comment-tools-25467" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25467-form-container" class="comment-form-container">
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

<span id="25469"></span>

<div id="answer-container-25469" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25469-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-25469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To get the normal, zooamble map, you could take and adopt the source code of the <a href="http://overpass-api.de/locate_me.html">Locate Me</a> prototype.</p>
<p>For the tagging: No such category exists in OSM so far. You can invent a new tag and just use it, for example "company=tech_startup" or whatever else rather then bend an existing one.</p>
<p>In general, it is easy to convert all objects of a certain tag to another tag later, but it is hard to disentagle different types of objects with the same tagging. For that reason, for more than a dozen objects, a new tag is highly appreciated.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '13, 07:33</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-25469" class="comments-container">
<span id="25481"></span>
<div id="comment-25481" class="comment">
<div id="post-25481-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"company=*" ? Any reason to not reuse the "office" tag here ?</p>
</div>
<div id="comment-25481-info" class="comment-info">
<span class="comment-age">(16 Aug '13, 13:25)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="25483"></span>
<div id="comment-25483" class="comment">
<div id="post-25483-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not a particular reason. I flipped with <a href="http://taginfo.openstreetmap.org">http://taginfo.openstreetmap.org</a> through the top 100 tags and found nothing suitable. As "office" has anyway "company" as most often appearing value, I suggest to follow the practice of key chaining (use the value of the more general key as special key, e.g. "type=route", "route=bus") and combine both: "office=company" + "company=tech_startup".</p>
</div>
<div id="comment-25483-info" class="comment-info">
<span class="comment-age">(16 Aug '13, 14:51)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
<span id="25580"></span>
<div id="comment-25580" class="comment">
<div id="post-25580-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also please document your new tag in the osm wiki for others to refer to. Also include any rules that you make up to whatever is a 'tech company'.</p>
</div>
<div id="comment-25580-info" class="comment-info">
<span class="comment-age">(19 Aug '13, 16:41)</span> <span class="comment-user userinfo">Chaos99</span>
</div>
</div>
<span id="25625"></span>
<div id="comment-25625" class="comment">
<div id="post-25625-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Then almost all existing values of "office=<em>" could be changed to "office=company" + "company=</em>" like architects or lawyers. I think the tag is intended to present a long range of values, like eg 'shops'. So "office=tech_startup". And since we try to avoid abbreviations in tags because we are not all geeks, "office=technology_startup" is even better.</p>
</div>
<div id="comment-25625-info" class="comment-info">
<span class="comment-age">(21 Aug '13, 16:51)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-25469" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25469-form-container" class="comment-form-container">
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

