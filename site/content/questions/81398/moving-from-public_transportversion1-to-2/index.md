+++
type = "question"
title = "moving from public_transport:version=1 to 2"
description = '''Hi there. I&#x27;m looking for help to understand and correct a route=bus relationship. I am not the original author, it was created recently according to the old public_transport:version=1. I just tried to understand its content and I translated it into version=2. In the process, since the description m...'''
date = "2021-08-20T21:43:00Z"
lastmod = "2021-08-31T20:44:00Z"
weight = 81398
keywords = [ "routing" ]
aliases = [ "/questions/81398" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [moving from public_transport:version=1 to 2](/questions/81398/moving-from-public_transportversion1-to-2)

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
<span id="post-81398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81398-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there. I'm looking for help to understand and correct a <code>route=bus</code> relationship.</p>
<p>I am not the original author, it was created recently according to the old <code>public_transport:version=1</code>. I just tried to understand its content and I translated it into <code>version=2</code>. In the process, since the description mentioned "from &lt;a&gt; to &lt;b&gt; and viceversa", I also split it into a forward and a return route, and the original author wrote about my intervention that I have destroyed three months worth of his work.</p>
<p>Could it be that someone helps us understand each other, my primary objective being to have correct data in our database? We are talking about the city of David in Chiriquí, Panama, and the relationships in question are in <a href="https://www.openstreetmap.org/changeset/106355316">this changeset</a>. Version 22, the last one before my first intervention, I have it saved, if someone wants to review it. Thank you very much in advance for the support or any suggestions.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '21, 21:43</strong></p>
<img src="https://secure.gravatar.com/avatar/482a09a1d3540beaa18993d358753a34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mariotomo&#39;s gravatar image" />
<p><span>mariotomo</span><br />
<span class="score" title="300 reputation points">300</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mariotomo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Aug '21, 21:54</strong> </span></p>
</div>
</div>
<div id="comments-container-81398" class="comments-container">
<span id="81399"></span>
<div id="comment-81399" class="comment">
<div id="post-81399-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This seems more like a question for the DWG. The extent to which the more complicated "v2" depreciates "v1" has been debated on several occasions.</p>
</div>
<div id="comment-81399-info" class="comment-info">
<span class="comment-age">(21 Aug '21, 01:38)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="81406"></span>
<div id="comment-81406" class="comment">
<div id="post-81406-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>From the comments in the changeset description, I am not clear how this route operates in reality. Does it have separate outward and return legs with two identifiable terminus stops, or is it one continuous loop starting and finishing at a single terminus? In my city both types exist, the latter are mapped with a single relation, even with PTv2.</p>
</div>
<div id="comment-81406-info" class="comment-info">
<span class="comment-age">(21 Aug '21, 12:05)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="81585"></span>
<div id="comment-81585" class="comment">
<div id="post-81585-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi and thanks for having a look at this. my question is possibly not about mapping but about communication between mappers. I still do not know what is the route, I only know that the original author "fixed" it by breaking it again, complaining about my edits, but not looking at the syntactical mistakes he introduced. if we don't speak the same language (Spanish, English, or public_transport:version=2), we can't understand each other.</p>
</div>
<div id="comment-81585-info" class="comment-info">
<span class="comment-age">(31 Aug '21, 17:01)</span> <span class="comment-user userinfo">mariotomo</span>
</div>
</div>
<span id="81591"></span>
<div id="comment-81591" class="comment">
<div id="post-81591-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If I understand the sequence of changeset comments correctly, a local mapper has been mapping a number of bus routes in David using the original public transport scheme ("PTv1"). You want to change this to PTv2, and in fact have made this change yourself for at least some routes.</p>
<p>Neither of these approaches is "wrong" - the main public transport page (in English at least) says that PTv1 is still widely used and has not been deprecated. In particular, while you seem to insist that separate relations should be used for "out" and "back" routes, it is standard practice in PTv1 to use a single relation.</p>
<p>I may have missed something, but I don't see any comment where you have explained why the routes should be changed to PTv2. Did you discuss or explain this at some point? As you are apparently not familiar with the routes yourself, and will presumably not be maintaining them in future, I feel it is up to you to make a clear argument for why PTv2 is better.</p>
<p>Of course if there are actual errors in the route relations (e.g. gaps), it is valid to point them out, but that is a separate issue from the choice of PTv1 or PTv2.</p>
</div>
<div id="comment-81591-info" class="comment-info">
<span class="comment-age">(31 Aug '21, 20:32)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="81592"></span>
<div id="comment-81592" class="comment">
<div id="post-81592-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hi Alan. I made a video to show the order in which objects were added to the original relation: <a href="https://i.imgur.com/GsAAvGY.mp4">https://i.imgur.com/GsAAvGY.mp4</a> … why do I insist/suggest to use PTv2, mostly because of the automatic QA offered by geofabrik.de. but also: (1) I do not know of a validator for PTv1, (2) while in contact with MiBus from Panama City we agreed to move to PTv2 (I do not recall the details, maybe it was just me suggesting and nobody telling me not to. anyhow, the contact with MiBus is currently lost) and I had converted some of the lines to it, (3) I suggest we use one style in the same country.</p>
<p>in short: since nobody else reviews anything here, I wish to learn only one style, and to rely upon automatic QA.</p>
</div>
<div id="comment-81592-info" class="comment-info">
<span class="comment-age">(31 Aug '21, 20:44)</span> <span class="comment-user userinfo">mariotomo</span>
</div>
</div>
</div>
<div id="comment-tools-81398" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81398-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

