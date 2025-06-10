+++
type = "question"
title = "Do you have a technique for quickly adding addr:street to many houses?"
description = '''In my area, most of the building outlines which exist don&#x27;t have address data. I use StreetComplete to collect addr:housenumber, but I don&#x27;t like using StreetComplete for doing addr:street because it&#x27;s very repetitive to tap on each house and then the street. In JOSM, I can do it a little faster, bu...'''
date = "2021-10-23T20:19:00Z"
lastmod = "2021-10-25T04:41:00Z"
weight = 82323
keywords = [ "josm", "streetcomplete", "streets", "address" ]
aliases = [ "/questions/82323" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Do you have a technique for quickly adding addr:street to many houses?](/questions/82323/do-you-have-a-technique-for-quickly-adding-addrstreet-to-many-houses)

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
<span id="post-82323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82323-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my area, most of the building outlines which exist don't have address data.</p>
<p>I use StreetComplete to collect addr:housenumber, but I don't like using StreetComplete for doing addr:street because it's very repetitive to tap on each house and then the street.</p>
<p>In JOSM, I can do it a little faster, but it's still not great:</p>
<ol>
<li>Select the street, double-click on the name tag to open the edit dialog so I can copy the name.</li>
<li>Select the houses using shift-click or a few lassos.</li>
<li>Click the "address" preset button on my top toolbar.</li>
<li>Delete the remembered text in the addr:street field and paste the new text there.</li>
</ol>
<p>This process is kind of slow though because it involves opening and dismissing two separate dialogs, and selecting the houses can be tedious because the curvature of the street can make it difficult to lasso the houses without catching other things by accident. I am already using filters to hide everything except the houses and streets.</p>
<p>I would like to know if members of the community have any other tools or techniques for quickly adding addr:street in cases where it is very obvious simply by looking at the aerials. I usually skip the houses on corners and do those with StreetComplete, but on the straight parts of the road it's pretty obvious what the addr:street is.</p>
<p>I am imagining a tool like a paintbrush where I can click the street, then drag my mouse over a bunch of houses without having to aim too much, and they will all get tagged just by painting over them.</p>
<p>Thanks for your time.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-streetcomplete" rel="tag" title="see questions tagged &#39;streetcomplete&#39;">streetcomplete</span> <span class="post-tag tag-link-streets" rel="tag" title="see questions tagged &#39;streets&#39;">streets</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '21, 20:19</strong></p>
<img src="https://secure.gravatar.com/avatar/1016cb75adfd12cc8c01e342bbaf979a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="traditionalstonethrow&#39;s gravatar image" />
<p><span>traditionals...</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="traditionalstonethrow has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82323" class="comments-container">
&#10;</div>
<div id="comment-tools-82323" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82323-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="82327"></span>

<div id="answer-container-82327" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82327-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are days when I wish JOSM had the option to choose between crossing select and window select.</p>
<p>In the absence of that, I think you can draw a dummy way and use <code>I</code> to select intersecting ways and delete the dummy way when done.</p>
<p>If you're doing your first pass with StreetComplete, then the house whose street you entered on location will probably have the tag prefilled and you can just edit that tag directly and apply to the relevant items.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '21, 21:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-82327" class="comments-container">
<span id="82329"></span>
<div id="comment-82329" class="comment">
<div id="post-82329-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your suggestions. Due to your answer I discovered the UtilsPlugin2 which contains the 'I' shortcut and a few other tools that I might find handy for some other things.</p>
<p>To clarify, I avoid doing addr:street on StreetComplete as much as possible. I only use StreetComplete to finish up the houses on corners, where I am not sure which street the house really belongs to when looking at the aerials.</p>
</div>
<div id="comment-82329-info" class="comment-info">
<span class="comment-age">(23 Oct '21, 21:16)</span> <span class="comment-user userinfo">traditionals...</span>
</div>
</div>
<span id="82333"></span>
<div id="comment-82333" class="comment">
<div id="post-82333-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/19438/traditionalstonethrow"></a><a href="https://help.openstreetmap.org/users/19438/traditionalstonethrow">@traditionalstonethrow</a> The plugin has the select All Inside area function. Relatedly, there have been requests for a draw buffer area tool found in standard GIS software, which may possibly be extended to select inside buffer.</p>
</div>
<div id="comment-82333-info" class="comment-info">
<span class="comment-age">(24 Oct '21, 05:04)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="82343"></span>
<div id="comment-82343" class="comment">
<div id="post-82343-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16887/kovoschiz">@Kovoschiz</a> if you're selecting adjacent buildings the parallel way tool will get you a line that can be used for intersect selection, but this will also pick up the branching streets. I think buffer would too?</p>
</div>
<div id="comment-82343-info" class="comment-info">
<span class="comment-age">(24 Oct '21, 14:52)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="82349"></span>
<div id="comment-82349" class="comment">
<div id="post-82349-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I haven't tried it outside. I imagine using area should limit the selection inside to lines completely inside. This should reduce the roads selected, depending on building size and details in the region. That being said, you are going to search for <code>building=*</code> inside your selection anyway. <a href="https://help.openstreetmap.org/users/11443/allroads"></a><a href="https://help.openstreetmap.org/users/11443/allroads">@Allroads</a> answered you can set up a filter showing streets and buildings only.</p>
</div>
<div id="comment-82349-info" class="comment-info">
<span class="comment-age">(25 Oct '21, 04:36)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="82350"></span>
<div id="comment-82350" class="comment">
<div id="post-82350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I doubt the intersecting method would be reliable for arbitrary building position and size.</p>
</div>
<div id="comment-82350-info" class="comment-info">
<span class="comment-age">(25 Oct '21, 04:41)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-82327" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82327-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82335"></span>

<div id="answer-container-82335" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82335-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In this context I'd also like to point you to the <a href="https://josm.openstreetmap.de/wiki/Styles/Coloured_Streets">Coloured Streets</a> map style in JOSM which provides visual feedback on missing and wrong address tagging and to the <a href="https://josm.openstreetmap.de/wiki/Help/Plugin/HouseNumberTaggingTool">House Number Tagging Tool</a> should you at one time want to tag house numbers with JOSM and not StreetComplete.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '21, 07:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-82335" class="comments-container">
<span id="82336"></span>
<div id="comment-82336" class="comment">
<div id="post-82336-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much for mentioning Coloured Strets, that looks like an awesome debugging tool.</p>
<p>In my area, house numbers do not count by +1 or +2, they are impossible for me to predict by aerials even when immediate neighbors are known.</p>
</div>
<div id="comment-82336-info" class="comment-info">
<span class="comment-age">(24 Oct '21, 07:37)</span> <span class="comment-user userinfo">traditionals...</span>
</div>
</div>
</div>
<div id="comment-tools-82335" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82335-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82328"></span>

<div id="answer-container-82328" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82328-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Partly the answer:</p>
<p>Select street, then in tags box click on tag name (now it is blue) then on the blue, right click, then copy value or key value, this is then on the clipboard. Make a tag on a building and then in the blue addr:street, rightclick and copy Selected 1Key/value and do the other buildings.</p>
<p>Using lasso, select buildings but not the building corner nodes shift-U deselecting nodes</p>
<p>Use the 3 + icon button paste tags or ctrl-shift-V <a href="https://josm.openstreetmap.de/wiki/Help/Menu/Edit">https://josm.openstreetmap.de/wiki/Help/Menu/Edit</a> <a href="https://josm.openstreetmap.de/wiki/Help/Action/PasteTags">https://josm.openstreetmap.de/wiki/Help/Action/PasteTags</a></p>
<p>You can set a filter in JOSM for only seeing the buildings, then lasso works better. Or only building and highway in the filter.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '21, 21:12</strong></p>
<img src="https://secure.gravatar.com/avatar/6c5dc0fc3be6786b643d15ec99ba3e3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Allroads&#39;s gravatar image" />
<p><span>Allroads</span><br />
<span class="score" title="222 reputation points">222</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Allroads has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-82328" class="comments-container">
<span id="82330"></span>
<div id="comment-82330" class="comment">
<div id="post-82330-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This seems almost identical to the process I described, but thank you for pointing out that the context menu allows copying the street's name without opening the dialog for it.</p>
</div>
<div id="comment-82330-info" class="comment-info">
<span class="comment-age">(23 Oct '21, 21:36)</span> <span class="comment-user userinfo">traditionals...</span>
</div>
</div>
</div>
<div id="comment-tools-82328" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82328-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82347"></span>

<div id="answer-container-82347" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82347-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For what it is worth, JOSM will use the near by street names when making suggestions as you type a value for the addr:street tag. I usually just select the houses on the street, click on the plus for adding a tag. If I have been doing this for other streets the addr:street tag is suggested and I just start typing the street name. Usually the correct one shows up within a few key strokes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '21, 03:26</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-82347" class="comments-container">
&#10;</div>
<div id="comment-tools-82347" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82347-form-container" class="comment-form-container">
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

