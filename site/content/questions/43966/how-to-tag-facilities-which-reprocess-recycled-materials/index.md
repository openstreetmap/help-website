+++
type = "question"
title = "How to tag facilities which reprocess recycled materials?"
description = '''I&#x27;d like to be able to tag facilities that do specific processing of recyclates, such as those listed here. A Materials Recovery Facility, or MRF, is a common one these days. man_made=works could be used but is very general. I dont think it is an amenity so amenity=recycling doesn&#x27;t seem right. Howe...'''
date = "2015-07-03T23:37:00Z"
lastmod = "2015-07-04T13:21:00Z"
weight = 43966
keywords = [ "works", "tagging" ]
aliases = [ "/questions/43966" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag facilities which reprocess recycled materials?](/questions/43966/how-to-tag-facilities-which-reprocess-recycled-materials)

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
<span id="post-43966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43966-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to be able to tag facilities that do specific processing of recyclates, such as those listed <a href="http://www.veolia.co.uk/our-services/our-services/recycling-and-waste-services/facilities">here</a>. A Materials Recovery Facility, or MRF, is a common one these days. <code>man_made=works</code> could be used but is very general. I dont think it is an <code>amenity</code> so <code>amenity=recycling</code> doesn't seem right. However extending <code>recycling</code> to <code>recycling=materials_recycling_facility</code> could be logical.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-works" rel="tag" title="see questions tagged &#39;works&#39;">works</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jul '15, 23:37</strong></p>
<img src="https://secure.gravatar.com/avatar/5a189d61db7b529d641746a2f4dc7aff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pmackay&#39;s gravatar image" />
<p><span>pmackay</span><br />
<span class="score" title="66 reputation points">66</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pmackay has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '15, 12:11</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-43966" class="comments-container">
&#10;</div>
<div id="comment-tools-43966" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43966-form-container" class="comment-form-container">
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

<span id="43974"></span>

<div id="answer-container-43974" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43974-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-43974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I went with just man_made=works on <a href="http://www.openstreetmap.org/way/310864914">one near me</a>. You can use whatever tags you like, so it's perfectly OK to make something up and use that as a lower-level key,</p>
<p>However, obviously it helps to try and find one that's already been used to mean the same thing, so you can see what values people have used previously for <a href="http://taginfo.openstreetmap.org/keys/works#values">"works"</a>, and also perhaps <a href="http://taginfo.openstreetmap.org/keys/industrial#values">"industrial"</a>, to see if anything fits. Also of course search keys and values for <a href="http://taginfo.openstreetmap.org/search?q=recycling#keys">"recycling"</a> - there might be something there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '15, 09:51</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-43974" class="comments-container">
<span id="43975"></span>
<div id="comment-43975" class="comment">
<div id="post-43975-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I appreciate I can add anything, I'm hoping for some tips on what might be a better way if I was to use new tags. I'd like to propose something at some point.</p>
<p>Seems like the <code>recycling</code> tag is mostly used for types of things. I think what this really needs is another level of detail on <code>man_made=works</code>. E.g. what about <code>works:type=materials_processing_facility</code>?</p>
</div>
<div id="comment-43975-info" class="comment-info">
<span class="comment-age">(04 Jul '15, 09:57)</span> <span class="comment-user userinfo">pmackay</span>
</div>
</div>
<span id="43976"></span>
<div id="comment-43976" class="comment">
<div id="post-43976-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"works" has slightly more usage as a key than "works:type" so I'd probably go with that instead, but "materials_processing_facility" sounds fine to me.</p>
</div>
<div id="comment-43976-info" class="comment-info">
<span class="comment-age">(04 Jul '15, 10:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="43981"></span>
<div id="comment-43981" class="comment">
<div id="post-43981-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, I hadnt realised that <code>works</code> is used as a key as well. Its not referenced on the <a href="http://wiki.openstreetmap.org/wiki/Tag:man_made%3Dworks">man_made=works</a> page.</p>
<p>To get a new wiki page for <code>tag:works</code> does it need to be setup as a Proposal or can a documentation page just be created?</p>
</div>
<div id="comment-43981-info" class="comment-info">
<span class="comment-age">(04 Jul '15, 13:04)</span> <span class="comment-user userinfo">pmackay</span>
</div>
</div>
<span id="43983"></span>
<div id="comment-43983" class="comment">
<div id="post-43983-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Re proposals vs wiki pages vs "JFDI", different people have different approaches - see the tagging list ad nauseam, including this recent discussion - <a href="https://lists.openstreetmap.org/pipermail/tagging/2015-March/thread.html#22382">https://lists.openstreetmap.org/pipermail/tagging/2015-March/thread.html#22382</a> .</p>
<p>I personally see no problem with creating a page for "tag:works" right now that describes how people use that tag. Discussion is also helpful, and maybe there are people on the tagging list who could suggest "I tagged one of these like X". In fact, there was a recent discussion that mentioned man_made=works, so there has been some recent interest:</p>
<p><a href="https://lists.openstreetmap.org/pipermail/tagging/2015-June/thread.html#25087">https://lists.openstreetmap.org/pipermail/tagging/2015-June/thread.html#25087</a></p>
<p>If I do have a problem with some of the tagging list traffic (and some wiki tag pages) it's that there are people often say "you should tag X like Y" where they have no experience of what "X" is and "Y" is something that no-one actually does, or they make statements about what OSM tags are used for in their corner of the world and assume there everywhere in the world is like their home region. However this isn't true of everyone/everything there, and the fact that people are trying to improve OSM tagging has got to be good.</p>
</div>
<div id="comment-43983-info" class="comment-info">
<span class="comment-age">(04 Jul '15, 13:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-43974" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43974-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43968"></span>

<div id="answer-container-43968" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43968-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure if I get the point, but sounds like <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Drecycling">amenity=recycling , recycling_type=centre, ...</a> to me?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '15, 07:31</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-43968" class="comments-container">
<span id="43969"></span>
<div id="comment-43969" class="comment">
<div id="post-43969-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I dont think those work, because a facility that <strong>processes</strong> recyclates is not a community "amenity" that citizens use directly. I think <code>recycling_type=centre</code> is for places where citizens can dump different types of waste.</p>
</div>
<div id="comment-43969-info" class="comment-info">
<span class="comment-age">(04 Jul '15, 07:39)</span> <span class="comment-user userinfo">pmackay</span>
</div>
</div>
</div>
<div id="comment-tools-43968" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43968-form-container" class="comment-form-container">
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

