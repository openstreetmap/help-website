+++
type = "question"
title = "Transport: Stop Area relations - What are they for?"
description = '''Hi I&#x27;ve been updating some UK railway stations, &amp;amp; was reading up on Stop Area What benefit is there in having what appears to be quite random items (bike parking, cafes etc) in a relation? I thought creating relations as a &#x27;collection of things&#x27; was discouraged. To me, all the relevant tags to i...'''
date = "2018-06-03T22:36:00Z"
lastmod = "2018-06-06T23:57:00Z"
weight = 63991
keywords = [ "public-transport", "stop_area", "relations" ]
aliases = [ "/questions/63991" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Transport: Stop Area relations - What are they for?](/questions/63991/transport-stop-area-relations-what-are-they-for)

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
<span id="post-63991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63991-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-63991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I've been updating some UK railway stations, &amp; was reading up on <a href="https://wiki.openstreetmap.org/wiki/Tag:public_transport%3Dstop_area">Stop Area</a></p>
<p>What benefit is there in having what appears to be quite random items (bike parking, cafes etc) in a <a href="https://www.openstreetmap.org/relation/4713070#map=17/51.26848/-1.08883">relation</a>? I thought creating relations as a 'collection of things' was discouraged.</p>
<p>To me, all the relevant tags to indicate where a transport stop is are much easily accessible in a node on the highway/railway, or am I missing something?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-stop_area" rel="tag" title="see questions tagged &#39;stop_area&#39;">stop_area</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '18, 22:36</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-63991" class="comments-container">
<span id="63992"></span>
<div id="comment-63992" class="comment">
<div id="post-63992-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>To be honest, the current public transport scheme seems very complicated to me: you need to make a route relation for each direction (gathering ways + stops + platforms), another mega-relation (type=route_master) for the whole, and here I'm seeing that for each stop area you need to gather elements in a relation too, right? That being said, editing relations is often frustrating and time taking.</p>
</div>
<div id="comment-63992-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 05:44)</span> <span class="comment-user userinfo">Privatemajory</span>
</div>
</div>
<span id="64022"></span>
<div id="comment-64022" class="comment">
<div id="post-64022-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I concur it's very complicated, which is disappointing as it discourages contribution &amp; leads to more errors. Adding irrelevances such as telephones, just makes it worse.</p>
</div>
<div id="comment-64022-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 16:12)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-63991" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63991-form-container" class="comment-form-container">
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

<span id="64058"></span>

<div id="answer-container-64058" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64058-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm iffy on the idea of amenities as members of a <code>public_transport=stop_area</code> relation. If the cafe or bicycle parking is available to the general public even when they're not currently using the transport in question, it's an unhelpful confusion to map it as part of the transport relation.</p>
<p>I see that the wiki (currently) disagrees and mentions in particular <code>taxi</code> and <code>bicycle_parking</code> as suggested relation members. Offhand I can't picture a station design where these amenities would be restricted to transport users. Maybe at a ferry or airport?</p>
<p>Some metro stations do include a cafe or fast food or vending machine or atm... I can see the case for these being part of the transport relation -- <strong><em>if</em></strong> they're located in an area only accessible to those who've paid a fare. I think tagging these with <code>access=customers</code> would also be appropriate, or maybe invent something more explicit like <code>access=transport_customers</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '18, 16:41</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-64058" class="comments-container">
<span id="64061"></span>
<div id="comment-64061" class="comment">
<div id="post-64061-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Likewise I can't imagine transport users being unable to locate these facilities if they're not included. I think someone got a bit trigger-happy conceiving this scheme. I note on the transit forum there's a discussion about simplifying it.</p>
</div>
<div id="comment-64061-info" class="comment-info">
<span class="comment-age">(06 Jun '18, 18:11)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="64068"></span>
<div id="comment-64068" class="comment">
<div id="post-64068-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah I've been waiting for that to shake out. Until then I haven't been doing any public transport in my area, which is currently tagged up a dozen different ways and desperately needs some sanity.</p>
<p>When the dust settles, then we can ponder about what scheme is best to indicate that certain amenities are for ticketed passengers only. In general, I feel that jamming them into transport relations is an awkward approach.</p>
</div>
<div id="comment-64068-info" class="comment-info">
<span class="comment-age">(06 Jun '18, 23:57)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-64058" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64058-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64049"></span>

<div id="answer-container-64049" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64049-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have answered this and other of your questions on the Talk-transit mailing list, see <a href="https://lists.openstreetmap.org/pipermail/talk-transit/2018-June/001929.html">https://lists.openstreetmap.org/pipermail/talk-transit/2018-June/001929.html</a></p>
<p>I would be nice if you ask your questions only at one location simultaneously. Thank you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '18, 12:54</strong></p>
<img src="https://secure.gravatar.com/avatar/d2a3b905e2632430b47dd9b8de3d8ba0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nakaner&#39;s gravatar image" />
<p><span>Nakaner</span><br />
<span class="score" title="610 reputation points">610</span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nakaner has 3 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jun '18, 13:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-64049" class="comments-container">
<span id="64050"></span>
<div id="comment-64050" class="comment">
<div id="post-64050-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>They are separate forums. I'm not cross-posting. Many contributors here, don't subscribe to Talk-Transit. I've noticed specific OSM newsfeed/Github forums get very protectionist in their responses such as 'how dare you criticise' &amp; '...but that's how we've always done it'. To get as varied &amp; accurate responses as possible I will ask in as many forums as I wish. Thank you for your response on the other thread.</p>
</div>
<div id="comment-64050-info" class="comment-info">
<span class="comment-age">(06 Jun '18, 13:14)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="64051"></span>
<div id="comment-64051" class="comment">
<div id="post-64051-score" class="comment-score">
4
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8569/nakaner">@Nakaner</a>, meta responses about cross-posting as first line of an answer are not very helpful for users here. <a href="https://help.openstreetmap.org/users/4225/dave">@Dave</a> F is quite right in that many more people will see answers here than in talk-transit, therefore a complaint about cross-posting as the first response is not appropriate. Please use comments only to highlight cross-posting (which is useful as it can save someone the effort of writing a reply when the question has already been answered). I have therefore moved it to the end of your reply.</p>
</div>
<div id="comment-64051-info" class="comment-info">
<span class="comment-age">(06 Jun '18, 13:42)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="64059"></span>
<div id="comment-64059" class="comment">
<div id="post-64059-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Cross-posting is fine as long as you mention in each platform the other places where you've posted/emailed so the participants can see all of the responses of others. Otherwise, you get duplication of effort.</p>
</div>
<div id="comment-64059-info" class="comment-info">
<span class="comment-age">(06 Jun '18, 17:27)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="64060"></span>
<div id="comment-64060" class="comment">
<div id="post-64060-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is <em>not</em> cross posting. That is where one <em>same</em> post is sent to multiple newsfeeds. This is not a newsfeed, it is a separate forum. My posts were separate &amp; different. Participants should a able to determine if they already posted an answer to a similar query from the same user.</p>
</div>
<div id="comment-64060-info" class="comment-info">
<span class="comment-age">(06 Jun '18, 18:04)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="64062"></span>
<div id="comment-64062" class="comment">
<div id="post-64062-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, even if you don't want to semantically call it "cross-posting", you're still conducting parallel discussions about the same subject matter on different platforms where the participants in one aren't aware of the content of the other (until someone notices and mentions it). This wastes effort because different people may be unknowingly giving the same response when only one of those is necessary.</p>
</div>
<div id="comment-64062-info" class="comment-info">
<span class="comment-age">(06 Jun '18, 18:15)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-64049" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64049-form-container" class="comment-form-container">
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

