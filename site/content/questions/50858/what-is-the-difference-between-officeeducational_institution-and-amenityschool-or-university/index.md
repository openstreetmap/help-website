+++
type = "question"
title = "What is the difference between office=educational_institution and amenity=school or university?"
description = '''The wiki page for office=educational_institution states that it should be used on an &quot;organization offering formal education; for example, a school, college or university.&quot; This definition seems to me to be at odds with existing tags used for such places, namely amenity=school, amenity=university, a...'''
date = "2016-07-12T10:35:00Z"
lastmod = "2016-07-12T12:37:00Z"
weight = 50858
keywords = [ "tag" ]
aliases = [ "/questions/50858" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What is the difference between office=educational_institution and amenity=school or university?](/questions/50858/what-is-the-difference-between-officeeducational_institution-and-amenityschool-or-university)

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
<span id="post-50858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50858-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The <a href="http://wiki.openstreetmap.org/wiki/Tag:office%3Deducational_institution">wiki page</a> for <code>office=educational_institution</code> states that it should be used on an "organization offering formal education; for example, a school, college or university." This definition seems to me to be at odds with existing tags used for such places, namely <code>amenity=school</code>, <code>amenity=university</code>, and <code>amenity=college</code>. As I wrote on the <a href="http://wiki.openstreetmap.org/wiki/Talk:Tag:office%3Deducational_institution">Talk</a> page, the transaltion used by iD for the tag rather unfortunately coincides with the name given to public schools in some Spanish-speaking countries (i.e. <em>Institución Educativa</em> + some name), resulting in schools there not being tagged with amenity=school at all and only with office=educational_institution.</p>
<p>So, how does <code>office=educational_institution</code> differ from the existing <code>amenity=*</code> alternatives for such places?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '16, 10:35</strong></p>
<img src="https://secure.gravatar.com/avatar/8dfc06314659f45fae00cb945dae0de2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carciofo&#39;s gravatar image" />
<p><span>carciofo</span><br />
<span class="score" title="91 reputation points">91</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carciofo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jul '16, 10:36</strong> </span></p>
</div>
</div>
<div id="comments-container-50858" class="comments-container">
&#10;</div>
<div id="comment-tools-50858" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50858-form-container" class="comment-form-container">
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

<span id="50862"></span>

<div id="answer-container-50862" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50862-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="carciofo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A friend of mine works for a local university. One of his job is to ensure that rooms for lectures etc. are distributed sensibly among competing requirements (a popular course gets a bigger room, because more people turn up and a less popular course a smaller one, even though the same number of students might be enrolled).</p>
<p>I suspect that the intention of this tag was that, if mapped separately, the building he works in would be an "office=educational_institution" and the building with the rooms he books would be part of an "office=university".</p>
<p>However, looking at <a href="http://overpass-turbo.eu/s/hgl">usage locally</a>, it actually seems to be used as a bit of a catch-all for where other tags might not fit. For personal rendering purposes I just dumped it in a "<a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/style.lua#L1696">nonspecific offices</a>" category.</p>
<p>Also be aware of potential issus tagging non-campus and multi-site institutions. There's a local discussion of that <a href="https://www.openstreetmap.org/changeset/39622488">here</a> and <a href="https://lists.openstreetmap.org/pipermail/talk-gb/2015-May/thread.html#17455">here</a>. While Cambridge is a bit of an exception where university tagging is concerned, multi-site institutions abound and so you won't get a one-to-one mapping of amenity=university to "real world university".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '16, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-50862" class="comments-container">
<span id="50865"></span>
<div id="comment-50865" class="comment">
<div id="post-50865-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Right, thanks for the info. So this seems to be a rather specific tag, but iD ignores the <code>office</code> part entirely and focuses on the <strong>institution</strong> side of it. I'm not convinced that <code>educational_institution</code> is a good name for an office, but I'm more concerned about getting iD to stop suggesting &amp; applying this tag instead of <code>amenity=school</code> when someone searches for "educational institution". Even the icon displayed (a building) is more representative of an "institution" than an "office", so there's no way for the user to know (s)he's doing so. Any ideas on how to get that accomplished would be appreciated.</p>
</div>
<div id="comment-50865-info" class="comment-info">
<span class="comment-age">(12 Jul '16, 11:53)</span> <span class="comment-user userinfo">carciofo</span>
</div>
</div>
<span id="50868"></span>
<div id="comment-50868" class="comment">
<div id="post-50868-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For iD translation, see the answer to this question:</p>
<p><a href="https://help.openstreetmap.org/questions/23930/is-it-possible-to-use-id-in-another-language">https://help.openstreetmap.org/questions/23930/is-it-possible-to-use-id-in-another-language</a></p>
<p>iD also uses keywords (such as shop brand names) to suggest tags. The github repository is <a href="https://github.com/openstreetmap/iD">https://github.com/openstreetmap/iD</a> - probably more info there.</p>
</div>
<div id="comment-50868-info" class="comment-info">
<span class="comment-age">(12 Jul '16, 12:37)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50862" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50862-form-container" class="comment-form-container">
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

