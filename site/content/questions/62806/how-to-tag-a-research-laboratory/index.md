+++
type = "question"
title = "How to tag a research laboratory?"
description = '''Specifically an ecology/biology laboratory. A search on the wiki suggests:  amenity=vivarium (57 uses, although the definition shoud really include plants as well as animals) amenity=research_institute (330 uses) office=research (5019 uses)  A search on taginfo suggests:  undocumented key laboratory...'''
date = "2018-03-24T14:44:00Z"
lastmod = "2019-03-15T11:32:00Z"
weight = 62806
keywords = [ "laboratory", "tagging", "research" ]
aliases = [ "/questions/62806" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag a research laboratory?](/questions/62806/how-to-tag-a-research-laboratory)

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
<span id="post-62806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62806-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Specifically an ecology/biology laboratory.</p>
<p>A search on the wiki suggests:</p>
<ul>
<li><a href="https://wiki.openstreetmap.org/wiki/Tag:amenity=vivarium">amenity=vivarium</a> (57 uses, although the definition shoud really include plants as well as animals)</li>
<li><a href="https://wiki.openstreetmap.org/wiki/Tag:amenity=research_institute">amenity=research_institute</a> (330 uses)</li>
<li><a href="https://wiki.openstreetmap.org/wiki/Tag:office=research">office=research</a> (5019 uses)</li>
</ul>
<p>A search on taginfo suggests:</p>
<ul>
<li>undocumented key <a href="https://taginfo.openstreetmap.org/keys/laboratory#overview">laboratory=*</a> (130 uses)</li>
<li>room=laboratory (for indoor mapping)</li>
<li>undocumented tag <a href="https://taginfo.openstreetmap.org/tags/amenity=laboratory">amenity=laboratory</a> (79 uses)</li>
</ul>
<p>I'll probably use amenity=research_institute, office=research and laboratory=biology. Does any one have any other tagging ideas or know of any existing mapped laboratories in OSM?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-laboratory" rel="tag" title="see questions tagged &#39;laboratory&#39;">laboratory</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-research" rel="tag" title="see questions tagged &#39;research&#39;">research</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '18, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/9f18ba3d13472af00b3b6e2befad85e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lakedistrict&#39;s gravatar image" />
<p><span>lakedistrict</span><br />
<span class="score" title="221 reputation points">221</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lakedistrict has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-62806" class="comments-container">
&#10;</div>
<div id="comment-tools-62806" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62806-form-container" class="comment-form-container">
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

<span id="68364"></span>

<div id="answer-container-68364" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68364-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-68364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As someone who has worked in various research laboratories and an early (possibly the only) user of <code>amenity=research_institution</code> tag I would in general recommend use of a tag like this: <code>amenity=research_institute</code> is much more popular and clearly the two are synonyms, so the latter is to be preferred.</p>
<p>Most places describing themselves as laboratories will be of this type (e.g., Molecular Biology Laboratory, Cambridge), although some may be simply commercial service providers for healthcare or industrial testing. In general the latter may fit into office or landuse=industrial categories.</p>
<p>These remarks apply principally to scientific or engineering research, as humanties research bodies tend to be smaller and have a lower need for dedicated facilities. Research institutions may be academic, governmental or quasi-governmental , not-for-profit or commercial. Related things include the buildings occupied by learned societies and professional associations (in the UK mainly in London &amp; Edinburgh). Some GLAMs are related: specialist research libraries, extensive parts of national museums etc.</p>
<p>Another key is office=research, but this is clearly an inappropriate extension of use of the office tag as many research institutions will contain a limited amount of office space, and the tag will not reflect things like hazards (e.g. ones I've encountered: explosions, noxious chemicals, radiation, biohazards), that most space is taken up with non-office things like animal houses, laboratories, fields (for agriculture research), workshops.</p>
<p>I would keep the specific tag laboratory for a room or series of rooms within either a research or higher education institution (where they may be designated for research or teaching).</p>
<p>Note that vivarium as a term does not or should not relate to laboratories. Usually these are places in zoos or similar institutions designed for exhibiting live terrestrial animals and is formed analogously to aquarium. Faculties for keeping experimental animals are completely different.</p>
<p>Note: thanks to Max Erickson for pointing out that research_institute is more widely used than my original suggestion of research_institution.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '19, 14:53</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Mar '19, 11:36</strong> </span></p>
</div>
</div>
<div id="comments-container-68364" class="comments-container">
<span id="68365"></span>
<div id="comment-68365" class="comment">
<div id="post-68365-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You're right, office is the wrong tag to use and research institute is far better. The labs I had in mind were for <a href="http://www.fba.org.uk/">http://www.fba.org.uk/</a> and <a href="https://www.ceh.ac.uk/">https://www.ceh.ac.uk/</a> , but it looks like I never got around to fixing the tagging on them because I wanted to double check which building was which first with a survey. I'll add it to my 'needs surveying' to-do list. :)</p>
</div>
<div id="comment-68365-info" class="comment-info">
<span class="comment-age">(13 Mar '19, 15:40)</span> <span class="comment-user userinfo">lakedistrict</span>
</div>
</div>
<span id="68366"></span>
<div id="comment-68366" class="comment">
<div id="post-68366-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, I wondered if it was the FBA. The CEH, Wallingford happens to be one I've visited a couple of times in the recent past. Definitely a research_institute.</p>
</div>
<div id="comment-68366-info" class="comment-info">
<span class="comment-age">(13 Mar '19, 17:33)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="68378"></span>
<div id="comment-68378" class="comment">
<div id="post-68378-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just for clarity, there's a little bit of use of amenity=research_institution (29) and quite some more usage of amenity=research_institute (551).</p>
</div>
<div id="comment-68378-info" class="comment-info">
<span class="comment-age">(15 Mar '19, 02:09)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="68381"></span>
<div id="comment-68381" class="comment">
<div id="post-68381-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh thanks, will revise answer accordingly. I tagged the Jackson Lab site with research_institution=yes back in August 2009! And the.re was this proposal (see my comments) from earlier <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/research_institution">https://wiki.openstreetmap.org/wiki/Proposed_features/research_institution</a></p>
</div>
<div id="comment-68381-info" class="comment-info">
<span class="comment-age">(15 Mar '19, 11:32)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68364-form-container" class="comment-form-container">
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

