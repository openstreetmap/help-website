+++
type = "question"
title = "Investigating changesets"
description = '''I find that it&#x27;s very hard to understand what it happening in a changset, it&#x27;s easy to get an suspicion that something is amiss but it&#x27;s very hard to dig deeper. Does anyone have any scripts, methods or just tips that will help in investigating a changeset? The only two things I&#x27;ve find was:  OSM hi...'''
date = "2011-08-14T01:20:00Z"
lastmod = "2013-10-14T08:21:00Z"
weight = 7077
keywords = [ "changeset", "tools", "webservice", "history" ]
aliases = [ "/questions/7077" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Investigating changesets](/questions/7077/investigating-changesets)

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
<span id="post-7077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7077-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-7077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I find that it's very hard to understand what it happening in a changset, it's easy to get an suspicion that something is amiss but it's very hard to dig deeper. Does anyone have any scripts, methods or just tips that will help in investigating a changeset?</p>
<p>The only two things I've find was:</p>
<ul>
<li><a href="http://osmhv.openstreetmap.de/changeset.jsp?id=8987983">OSM history/changeset Vizualizer</a> which tries to declutter a changeset, with vectors on a map.</li>
<li><a href="http://wiki.openstreetmap.org/wiki/Osmdiff">osmdiff</a> renders a map and prints a report with all changed tags and geometries.</li>
</ul>
<p>Take this changeset on <a href="http://www.openstreetmap.org/browse/changeset/8987983">OSM main site</a> and on <a href="http://osmhv.openstreetmap.de/changeset.jsp?id=8987983">OSM History Vizualizer</a>, it's very hard to figure out exactly what happend. (I'm not pointing fingers at the creator of the changeset, I just haven't been bothered to find a changeset where I have recreated and removed lots of stuff.)</p>
<p>So to restate some questions.</p>
<ol>
<li>what do you look for when you look at a changeset?</li>
<li>is there a way to create the before.osm and after.osm files given a changeset ID. (to make osmdiff happy)</li>
<li>is there a similar changeset viewer like the one on the main site, that doesn't make you click "next page" all the time.?</li>
</ol>
<p>It might be a good idea to try to split up answers</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-tools" rel="tag" title="see questions tagged &#39;tools&#39;">tools</span> <span class="post-tag tag-link-webservice" rel="tag" title="see questions tagged &#39;webservice&#39;">webservice</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '11, 01:20</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '11, 09:09</strong> </span></p>
</div>
</div>
<div id="comments-container-7077" class="comments-container">
<span id="7080"></span>
<div id="comment-7080" class="comment">
<div id="post-7080-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If you know that the question should be discussed on the mailinglist why do you ask it here?</p>
</div>
<div id="comment-7080-info" class="comment-info">
<span class="comment-age">(14 Aug '11, 12:22)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="7081"></span>
<div id="comment-7081" class="comment">
<div id="post-7081-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This does not appear to be a question, rather the author wants to have a discussion.</p>
</div>
<div id="comment-7081-info" class="comment-info">
<span class="comment-age">(14 Aug '11, 13:00)</span> <span class="comment-user userinfo">emacsen</span>
</div>
</div>
<span id="7082"></span>
<div id="comment-7082" class="comment">
<div id="post-7082-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Might is not the same thing as "should". There must be people who have researched changesets and answers describing personal methods would really help. I do not think it warrants down votes just because it's hard to give good answers.</p>
</div>
<div id="comment-7082-info" class="comment-info">
<span class="comment-age">(14 Aug '11, 14:54)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="7099"></span>
<div id="comment-7099" class="comment">
<div id="post-7099-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I would quite like to know some people's answers to this question myself. From that point of view it's quite good. But yes, it's more of a discussion than an a specific question.</p>
</div>
<div id="comment-7099-info" class="comment-info">
<span class="comment-age">(15 Aug '11, 13:48)</span> <span class="comment-user userinfo">Harry Wood</span>
</div>
</div>
<span id="27138"></span>
<div id="comment-27138" class="comment">
<div id="post-27138-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for mentioning the history viewer. This is a great tool. I usually used itoWorld for this, but its updates take a week.</p>
</div>
<div id="comment-27138-info" class="comment-info">
<span class="comment-age">(14 Oct '13, 08:21)</span> <span class="comment-user userinfo">Chaos99</span>
</div>
</div>
</div>
<div id="comment-tools-7077" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7077-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

