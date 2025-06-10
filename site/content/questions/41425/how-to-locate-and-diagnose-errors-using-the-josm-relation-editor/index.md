+++
type = "question"
title = "How to locate and diagnose errors using the JOSM Relation Editor"
description = '''I received the dreaded &quot;multipolygon not closed&quot; error message recently. There was apparently a &quot;gap&quot; somewhere that prevented the 105-member multipolygon I was working on from compiling as it should. Try as I might I could not locate the error or gap or whatever the problem was by using any of the ...'''
date = "2015-02-28T10:43:00Z"
lastmod = "2015-03-02T15:24:00Z"
weight = 41425
keywords = [ "josm", "zoom", "relations", "gap" ]
aliases = [ "/questions/41425" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to locate and diagnose errors using the JOSM Relation Editor](/questions/41425/how-to-locate-and-diagnose-errors-using-the-josm-relation-editor)

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
<span id="post-41425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41425-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-41425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I received the dreaded "multipolygon not closed" error message recently. There was apparently a "gap" somewhere that prevented the 105-member multipolygon I was working on from compiling as it should. Try as I might I could not locate the error or gap or whatever the problem was by using any of the built-in functions of the Relation Editor. I was able to resolve the problem but the Relation Editor wasn't much help.</p>
<p>There is a function in the Relation Editor that is supposed to allow one to visualize, even to highlight, such a "gap" and perhaps it did that, but it never told me what sort of gap it was. I was looking for a place where I had forgotten to join two ways. That is the usual reason for such an error message. As it turned out, I had forgotten to change the role of a large way segment from inner to outer. But neither the message nor the Relation Editor UI gave me that critical piece of information.</p>
<p>The only readable mention besides patch reports in the JOSM Wiki about "zoom to gap" I was able to find was this: "When fixing larger (route-)relations it would be very helpful if there were buttons within the Relation Editor for jumping to the next or previous gap in the graph." I would add, and then add to the documentation a short description of how to use those buttons. A definition of exactly what a gap is would also help.</p>
<p>Taking a look at the Relation Editor dialog box on <a href="http://josm.openstreetmap.de/wiki/Help/Dialog/RelationEditor">this page</a>, we can see three columns in the the <em>Members</em> section at lower left. There are explanations that help me understand what <em>Role</em> and <em>Refers To</em> mean but what about the third column? I'm sure it has a useful function but I cannot determine what that might be. Also, on the far left there is a Sort button. Press it to sort the Members, Press it again to sort them in reverse. But what is the sorting based on? Moreover, why would one sort them in the first place?</p>
<p>The Relation Editor is a powerful tool that is, IMO, really not documented very well. Reading the Help pages is sort of like listening to a hundred TV News reports about a war. The overall story about how to use the tool effectively is hidden within a thousand small stories.</p>
<p>I'm not complaining about the tool itself or the people who wrote the code to implement it but I need to learn how to use it more effectively. Is there anyplace where this is all written down and explained?</p>
<p><a href="http://josm.openstreetmap.de/attachment/wiki/Help/Dialog/RelationEditor/relation_editor.png">Relation Editor window</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-gap" rel="tag" title="see questions tagged &#39;gap&#39;">gap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '15, 10:43</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-41425" class="comments-container">
<span id="41435"></span>
<div id="comment-41435" class="comment">
<div id="post-41435-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>An alternative (not JOSM and works only works if the relation is already uploaded): With <a href="http://ra.osmsurround.org/analyzeRelation">http://ra.osmsurround.org/analyzeRelation</a> you can see the gaps easily on a map (markers at all ends).</p>
</div>
<div id="comment-41435-info" class="comment-info">
<span class="comment-age">(01 Mar '15, 13:09)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41425" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41425-form-container" class="comment-form-container">
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

<span id="41434"></span>

<div id="answer-container-41434" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41434-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AlaskaDave has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not sure if I am understanding your problem correctly, but will try:</p>
<p>@"what about the third column": see <a href="https://josm.openstreetmap.de/wiki/Help/Dialog/RelationEditor">Help/Dialog/RelationEditor</a>: "on the right information about neighbor ways' connections useful for consistency checks like checking that the members of a multipolygon form closed ways or that a route is a complete line without missing some ways in the middle."</p>
<p>This only works in a useful way if the relation members are sorted. You can do that either manually or with the button which you have discovered. If I remember correctly: If you just press the button it sorts all the members. But you also could select only a part of the members (in the "Members" list) and then press it - then only those will be sorted. What the sorting does? From what I saw in the past it tries to sort them in a way that they are in an order which allows you do jump from one member to the next member. Meaning: the end nodes of a member way will be shared with the previous/next member way in the "Members" list.</p>
<p>The red points (see the "third column") mean that there is no connection to the prev/next member.</p>
<p><em>Addition:</em> Apparently you were quoting from (among others) <a href="https://josm.openstreetmap.de/ticket/7168">ticket 7168</a> ("Add a "jump to gap" functionality to the relation editor") – which has been implemented if I read correctly. I think I never used this function myself. Okay, I think I have found it: It is accessible via a right click in the "Members" list. But <em>seems</em> to only work with sorted members, it just searches for the next red point in the "third column". <em>/Addition</em></p>
<p>Just a general note: I think it is a good practise not to blindly click the sort button when you encounter a relation which appears to be slightly unsorted. At least check which type of relation it is, maybe check the history for comments.</p>
<p>And one more: Once you've understood the relation editor and tried a few times, please help to improve the JOSM help page. It is a wiki, you do not need to be a programmer to change it. Sign up, log in and edit.</p>
<p>The JOSM help should be the "place where this is all written down and explained". You will find a bit also at e.g. <a href="https://wiki.openstreetmap.org/wiki/JOSM/Advanced_editing#Relations">https://wiki.openstreetmap.org/wiki/JOSM/Advanced_editing#Relations</a> but that is more basic.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '15, 12:15</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Mar '15, 20:21</strong> </span></p>
</div>
</div>
<div id="comments-container-41434" class="comments-container">
<span id="41436"></span>
<div id="comment-41436" class="comment">
<div id="post-41436-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks asseerel, that's a help. I will try to educate myself more fully as I go and, should I gain enough experience and understanding, would definitely add some clarifications to the Wiki.</p>
<p>I will also give the <em>Relation Analyzer</em> a shot tomorrow.</p>
</div>
<div id="comment-41436-info" class="comment-info">
<span class="comment-age">(01 Mar '15, 13:14)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-41434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41434-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41428"></span>

<div id="answer-container-41428" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41428-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Alaska Dave, why going into the Relation Editor ? If you use JOSM, the build in tool validations with warnings; makes perfectly clear with yellow dots where the mistake can be found.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '15, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-41428" class="comments-container">
<span id="41433"></span>
<div id="comment-41433" class="comment">
<div id="post-41433-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Not really. In a a large relation with many members the yellow overlay is not enough to pinpoint where the error is. Nor do the yellow lines or error message indicate what the error is. In the case I mentioned the polygon was indeed "not closed" but it was because an inner member should have been an outer. A better error message would have saved much time.</p>
</div>
<div id="comment-41433-info" class="comment-info">
<span class="comment-age">(28 Feb '15, 23:45)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="41455"></span>
<div id="comment-41455" class="comment">
<div id="post-41455-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, looking at the yellow dots or ways solves the problem most of the time.</p>
</div>
<div id="comment-41455-info" class="comment-info">
<span class="comment-age">(02 Mar '15, 15:24)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-41428" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41428-form-container" class="comment-form-container">
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

