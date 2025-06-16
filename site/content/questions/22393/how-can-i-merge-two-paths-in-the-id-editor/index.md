+++
type = "question"
title = "How can I merge two paths in the iD editor?"
description = '''I&#x27;m trying to fix the information for a canal which was buried and covered with a multi-use trail. I used the iD editor to change the path&#x27;s metadata such as the name and type. It turns out that the canal was created as several separate paths, so my change only affected a small portion of the path. ...'''
date = "2013-05-13T21:57:00Z"
lastmod = "2022-08-30T21:06:00Z"
weight = 22393
keywords = [ "ideditor", "merging" ]
aliases = [ "/questions/22393" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How can I merge two paths in the iD editor?](/questions/22393/how-can-i-merge-two-paths-in-the-id-editor)

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
<span id="post-22393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22393-score" class="post-score" title="current number of votes">
10
</div>
<span id="post-22393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to fix the information for a canal which was buried and covered with a multi-use trail. I used the iD editor to change the path's metadata such as the name and type. It turns out that the canal was created as several separate paths, so my change only affected a small portion of the path.</p>
<p>Is it possible to merge the various portions of the path into a single path so that I don't have to make the same change 20 times?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-merging" rel="tag" title="see questions tagged &#39;merging&#39;">merging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 May '13, 21:57</strong></p>
<img src="https://secure.gravatar.com/avatar/3ce79c524c5c15936c7ba14bb4409e87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amcnabb8&#39;s gravatar image" />
<p><span>amcnabb8</span><br />
<span class="score" title="186 reputation points">186</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amcnabb8 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22393" class="comments-container">
<span id="22404"></span>
<div id="comment-22404" class="comment">
<div id="post-22404-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>take care to only merge if the single pieces of the path have the same tags (look at the bottom of the right panel after selecting a way at "all tags"). If iD does not recognize the tags then you may not see the difference. If you merge ways with different tags the resulting way simply has all the tags of the single ways with no warning issued. (<a href="https://github.com/systemed/iD/issues/1480">issue posted</a>)</p>
</div>
<div id="comment-22404-info" class="comment-info">
<span class="comment-age">(14 May '13, 00:33)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="25699"></span>
<div id="comment-25699" class="comment">
<div id="post-25699-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also for me both don't work. With Id I get the message lines are not connected and with Potlach 2 the chain symbol is not active. How do I connect the points? I thought they are.</p>
<p>76.52393 15.28646</p>
</div>
<div id="comment-25699-info" class="comment-info">
<span class="comment-age">(23 Aug '13, 20:29)</span> <span class="comment-user userinfo">ivolino</span>
</div>
</div>
<span id="25701"></span>
<div id="comment-25701" class="comment">
<div id="post-25701-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@ivolino</span> - Trying zooming in a bit further - you'll probably see that they're very close together, but not actually joined.</p>
</div>
<div id="comment-25701-info" class="comment-info">
<span class="comment-age">(23 Aug '13, 21:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="25726"></span>
<div id="comment-25726" class="comment not_top_scorer">
<div id="post-25726-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@ivolino</span> Perhaps you could explain a bit more what you're actually trying to do? (from reading the comments below) we're a bit confused!</p>
</div>
<div id="comment-25726-info" class="comment-info">
<span class="comment-age">(24 Aug '13, 12:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="25727"></span>
<div id="comment-25727" class="comment not_top_scorer">
<div id="post-25727-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I uploaded a GPS track. The track has some missing points and branches. I think I have 4 track parts which are 2 roads. Now I want to merge the 2 tracks to one road. I split one track so that there are only 2 lines. I tried all I never get this join. What do I wrong?</p>
</div>
<div id="comment-25727-info" class="comment-info">
<span class="comment-age">(24 Aug '13, 15:04)</span> <span class="comment-user userinfo">ivolino</span>
</div>
</div>
<span id="25728"></span>
<div id="comment-25728" class="comment not_top_scorer">
<div id="post-25728-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And it is confusing to mark the parts with shift in ID and control in Potlatch 2.</p>
</div>
<div id="comment-25728-info" class="comment-info">
<span class="comment-age">(24 Aug '13, 15:07)</span> <span class="comment-user userinfo">ivolino</span>
</div>
</div>
<span id="25729"></span>
<div id="comment-25729" class="comment">
<div id="post-25729-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ok I think I got it. It was not working because there was a branch. Now I split the branch and now I could merge the two tracks. That means a road can never have branches?<br />
</p>
</div>
<div id="comment-25729-info" class="comment-info">
<span class="comment-age">(24 Aug '13, 15:16)</span> <span class="comment-user userinfo">ivolino</span>
</div>
</div>
<span id="25730"></span>
<div id="comment-25730" class="comment not_top_scorer">
<div id="post-25730-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How do I know if I have successfully joined two points?</p>
</div>
<div id="comment-25730-info" class="comment-info">
<span class="comment-age">(24 Aug '13, 15:20)</span> <span class="comment-user userinfo">ivolino</span>
</div>
</div>
<span id="25731"></span>
<div id="comment-25731" class="comment not_top_scorer">
<div id="post-25731-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@ivolino</span> - You've already posted a link, so people can click on that to have a look. It looks joined and merged to me:</p>
<p><a href="https://www.openstreetmap.org/#map=18/15.28664/76.52334&amp;layers=D">https://www.openstreetmap.org/#map=18/15.28664/76.52334&amp;layers=D</a></p>
</div>
<div id="comment-25731-info" class="comment-info">
<span class="comment-age">(24 Aug '13, 15:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="25733"></span>
<div id="comment-25733" class="comment">
<div id="post-25733-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Select the node and wiggle it a bit, that will confirm connection.</p>
</div>
<div id="comment-25733-info" class="comment-info">
<span class="comment-age">(24 Aug '13, 16:15)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-22393" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-22393-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="22394"></span>

<div id="answer-container-22394" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22394-score" class="post-score" title="current number of votes">
11
</div>
<span id="post-22394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="amcnabb8 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Select one way, hold down Shift and select the next way: a + icon appears, and you can click this to merge the ways. Then Shift-click the next section and click the + icon again. And so on. You don't seem to be able to merge 3 or more ways at once.</p>
<p>Steve</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 May '13, 22:37</strong></p>
<img src="https://secure.gravatar.com/avatar/e3fd0c6e01ccf0d708c0d2fba9a03467?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sdoerr&#39;s gravatar image" />
<p><span>sdoerr</span><br />
<span class="score" title="1461 reputation points"><span>1.5k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sdoerr has 3 accepted answers">8%</span> </br></p>
</div>
</div>
<div id="comments-container-22394" class="comments-container">
<span id="22395"></span>
<div id="comment-22395" class="comment">
<div id="post-22395-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>That works. Thanks.</p>
</div>
<div id="comment-22395-info" class="comment-info">
<span class="comment-age">(13 May '13, 22:39)</span> <span class="comment-user userinfo">amcnabb8</span>
</div>
</div>
<span id="23785"></span>
<div id="comment-23785" class="comment">
<div id="post-23785-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I can't do that. It says that I cannot join the lines since they are not connected. That would make sense, but the lines actually <em>are</em> connected! If I drag the connection point around both lines changes, so that means that the lines are actually connected each other. Am I missing something? Thanks.</p>
</div>
<div id="comment-23785-info" class="comment-info">
<span class="comment-age">(28 Jun '13, 15:25)</span> <span class="comment-user userinfo">Febs</span>
</div>
</div>
<span id="23787"></span>
<div id="comment-23787" class="comment">
<div id="post-23787-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Could you perhaps add a link to the data that you're seeing this with?</p>
</div>
<div id="comment-23787-info" class="comment-info">
<span class="comment-age">(28 Jun '13, 16:00)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="25712"></span>
<div id="comment-25712" class="comment">
<div id="post-25712-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I zoomed as much in as possible but still I don't get the +. Do I just have to drag the one point on the other to connect the point or do I have to do more? Is there any sign that I can see if they are connected? Wow is this difficult.</p>
<p><a href="https://www.openstreetmap.org/edit?editor=id#map=24/15.28661/76.52399">https://www.openstreetmap.org/edit?editor=id#map=24/15.28661/76.52399</a></p>
</div>
<div id="comment-25712-info" class="comment-info">
<span class="comment-age">(24 Aug '13, 03:30)</span> <span class="comment-user userinfo">ivolino</span>
</div>
</div>
<span id="25722"></span>
<div id="comment-25722" class="comment not_top_scorer">
<div id="post-25722-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@ivolino</span>: A prerequisite to merging/combining <em>ways</em> is that they are <em>connected</em>!</p>
<ul>
<li>Step A - make the way be connected first (way are connected if they are sharing nodes): if you drag the node of the eastern way very near to the node of the western ways the nodes will have a red highlight around. After releasing the mouse button the nodes seem to be automatically merged. You can check that by dragging the node - all connected ways move then (be sure to undo that "test move" afterwards).</li>
<li>Step B - merge/combine ways (as mentioned by sdoerr above).</li>
</ul>
</div>
<div id="comment-25722-info" class="comment-info">
<span class="comment-age">(24 Aug '13, 12:34)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="25724"></span>
<div id="comment-25724" class="comment">
<div id="post-25724-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think that some of the answers are at cross-purposes here. The original question sounded like it was asking "how do I join two things together in the OSM database so that they become one thing". However, <span></span><span>@Ivolino</span>'s question seems to be "How do I join thing A to thing B so that e.g. routers know that you can get from one to the other".</p>
<p>To answer the second of these, I've just tried it <a href="http://api06.dev.openstreetmap.org/edit#map=18/53.10816/-0.51993">over on the dev server</a> and just dragging the road that joins the other one to the corner creates a join for me.<br />
</p>
<p>You can't (in any editor) join ways that together form a Y-shape together into one way the OSM database - ways are only ever lines, never branched.</p>
</div>
<div id="comment-25724-info" class="comment-info">
<span class="comment-age">(24 Aug '13, 12:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="25725"></span>
<div id="comment-25725" class="comment not_top_scorer">
<div id="post-25725-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@SomeoneElse</span>: I was surprised by the automatic node merging/joining, too. However, the question is about merging paths (usually named "combining").</p>
</div>
<div id="comment-25725-info" class="comment-info">
<span class="comment-age">(24 Aug '13, 12:54)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="51819"></span>
<div id="comment-51819" class="comment not_top_scorer">
<div id="post-51819-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's annoying not being to merge ways that together form a Y-shape. There's a lot of streets in the city I'm editing that are just like that, with multiple branches but all being one street. I have to edit all branches and give them the exact same name and features. It doesn't really make sense but I understand it's a technical limitation. I just hope that when you search for the street name you won't get one result per street's branch.</p>
</div>
<div id="comment-51819-info" class="comment-info">
<span class="comment-age">(30 Aug '16, 11:17)</span> <span class="comment-user userinfo">coolnodje</span>
</div>
</div>
<span id="85507"></span>
<div id="comment-85507" class="comment not_top_scorer">
<div id="post-85507-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Where does the plus sign appear? I don't see it except in the cursor when holding down Shift. (Aha! You have to right-click after selecting multiple ways.)</p>
</div>
<div id="comment-85507-info" class="comment-info">
<span class="comment-age">(30 Aug '22, 21:06)</span> <span class="comment-user userinfo">brightj</span>
</div>
</div>
</div>
<div id="comment-tools-22394" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-22394-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38416"></span>

<div id="answer-container-38416" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38416-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have to <strong>select all the ways</strong> you want to merge (<strong>without nodes</strong>) and then <strong>click the + icon in the ring menu</strong>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Nov '14, 20:40</strong></p>
<img src="https://secure.gravatar.com/avatar/d06aa11ce20e7b8a018c57951e0c2bea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keepright-ler&#39;s gravatar image" />
<p><span>keepright-ler</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keepright-ler has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-38416" class="comments-container">
&#10;</div>
<div id="comment-tools-38416" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38416-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82573"></span>

<div id="answer-container-82573" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82573-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe the editor used to work differently, but I have found I need to select the part of the path for which I have already set all the tags for, in the description menu on the left, then hold down a <strong>Shift</strong> key and click a part of the path adjacent to the selected portion, THEN <strong>Right-click</strong> the portion just selected... NOW the context menu with the <strong>+</strong> sign in it will appear so the 2 paths can be <strong>Merge</strong>d into 1 (complete with all the tags previously configured).</p>
<p>Even more convenient, when you get to the edge of the screen where you're drawing a line (<em>e.g.</em> following a GPS trace you've uploaded, to, say, document a trail that's not visible through the trees in satellite view), click <strong>and hold</strong> the last point near the edge while you drag the screen over, then you can continue that same line... without having to make a bunch of different lines and then <strong>Merge</strong> them.</p>
<p>Hope that helps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '21, 22:15</strong></p>
<img src="https://secure.gravatar.com/avatar/de65dadbc084577e5ebd38afd21933ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Darr247&#39;s gravatar image" />
<p><span>Darr247</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Darr247 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82573" class="comments-container">
&#10;</div>
<div id="comment-tools-82573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82573-form-container" class="comment-form-container">
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

