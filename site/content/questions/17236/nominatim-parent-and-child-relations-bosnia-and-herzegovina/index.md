+++
type = "question"
title = "Nominatim parent and child relations Bosnia and Herzegovina"
description = '''Hello, I was wondering if anybody can help me with the following issue. I was editing administrative boundaries within Bosnia and Herzegovina (adding entities, cantons, municipalities). I deleted the old boundaries (country and entities) so I could create completely new administrative network of B&amp;a...'''
date = "2012-10-28T19:53:00Z"
lastmod = "2012-12-02T20:28:00Z"
weight = 17236
keywords = [ "relation", "nominatim", "admin_boundary", "parent", "child" ]
aliases = [ "/questions/17236" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim parent and child relations Bosnia and Herzegovina](/questions/17236/nominatim-parent-and-child-relations-bosnia-and-herzegovina)

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
<span id="post-17236-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17236-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17236-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I was wondering if anybody can help me with the following issue.</p>
<p>I was editing administrative boundaries within Bosnia and Herzegovina (adding entities, cantons, municipalities). I deleted the old boundaries (country and entities) so I could create completely new administrative network of B&amp;H. Now, when I search Nominatim for Bosnia and Herzegovina, I get old, deleted relation of Bosnia and Herzegovina border, and not the one which I created (which is B6H admin lvl 2). Also, I saw in example of other countries that, after you search for a country, you get child relations (regions and municipalities).</p>
<p>Here is the changeset I have made (admin levels 2, 4, 5 and 6 - country, entities, cantons, municipalities):</p>
<p><a href="https://www.openstreetmap.org/browse/changeset/13633166">https://www.openstreetmap.org/browse/changeset/13633166</a></p>
<p>My question is, how to organize this new data (which is a lot richer) so it could show up in nominatim, first country, and then all child relations on the same page?</p>
<p>Best regards,</p>
<p>Alen</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-parent" rel="tag" title="see questions tagged &#39;parent&#39;">parent</span> <span class="post-tag tag-link-child" rel="tag" title="see questions tagged &#39;child&#39;">child</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '12, 19:53</strong></p>
<img src="https://secure.gravatar.com/avatar/c0fa352d1e54a3639614fd239fc88f94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alenmahovic&#39;s gravatar image" />
<p><span>alenmahovic</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alenmahovic has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17236" class="comments-container">
&#10;</div>
<div id="comment-tools-17236" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17236-form-container" class="comment-form-container">
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

<span id="18156"></span>

<div id="answer-container-18156" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18156-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-18156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim has a protection against mapping accidents. To avoid that entire countries suddenly disappear because somebody unintentionally deleted a boundary relation, it requires that an admin manually releases large boundary relations when they are deleted.</p>
<p>I've removed the two old relations for Bosnia-Herzegovina now. Things should sort themselves out shortly. In general, there is an <a href="http://nominatim.openstreetmap.org/deletable">up-to-date list of such objects</a>. If you find your deleted relations in there, just let me know and I'll release them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '12, 20:28</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-18156" class="comments-container">
&#10;</div>
<div id="comment-tools-18156" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18156-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17238"></span>

<div id="answer-container-17238" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17238-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Currently the result for Bosnia and Herzegovina is relation <a href="https://www.openstreetmap.org/browse/relation/2528142">2528142</a>, which is the new one.</p>
<p>You can read <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">boundary relations page</a> and decide whether you use or not the way that can be used for defining subareas.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '12, 20:26</strong></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RM87 has 20 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-17238" class="comments-container">
<span id="17323"></span>
<div id="comment-17323" class="comment">
<div id="post-17323-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am getting the old relation for BH which doesn't exist: 214908</p>
<p>BiH Federation child items are not complete (divided between relations 2321266 and 2528144) 2321266 was deleted.</p>
<p>RS child items are also not complete (divided between 2528145 and node 1987254376).</p>
<p>Brcko District is Ok i presume (relation 2528143)</p>
</div>
<div id="comment-17323-info" class="comment-info">
<span class="comment-age">(31 Oct '12, 13:15)</span> <span class="comment-user userinfo">alenmahovic</span>
</div>
</div>
<span id="17324"></span>
<div id="comment-17324" class="comment">
<div id="post-17324-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Problem is that even though old relations were deleted, and that new relations exist, results are not displayer correctly, respectively, child items of BiH F, RS and Brcko District are not all shown where they should be. New relations refer to all existing ways, old relations don't refer to existing ways, they don't exist at all.</p>
</div>
<div id="comment-17324-info" class="comment-info">
<span class="comment-age">(31 Oct '12, 13:15)</span> <span class="comment-user userinfo">alenmahovic</span>
</div>
</div>
<span id="17325"></span>
<div id="comment-17325" class="comment">
<div id="post-17325-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am just wondering how to organize everything so search in nominatim could show all child items under their respective relations (new ones). I am really confused here since I believe I organized relations correctly with outer ways, every last one of them. Ways for country of BiH were used also as ways for lower admin levels, such as entities, cantons, municipalities, ways of entities were also used as ways of cantons, ways of cantons were also used as ways of municipalities, and so on... (and I performed it very carefully not to forget even one of them).</p>
<p>Any assistance?</p>
<p>Regards,</p>
<p>Alen</p>
</div>
<div id="comment-17325-info" class="comment-info">
<span class="comment-age">(31 Oct '12, 13:16)</span> <span class="comment-user userinfo">alenmahovic</span>
</div>
</div>
</div>
<div id="comment-tools-17238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17238-form-container" class="comment-form-container">
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

