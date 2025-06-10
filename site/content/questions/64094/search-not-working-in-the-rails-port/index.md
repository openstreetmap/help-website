+++
type = "question"
title = "Search not working in The Rails Port"
description = '''Hello All, I have installed Rails port , from map point of view its working fine , Navigation works good.  only problem is Search is not working,  example if i type &quot;City of London&quot; then select one link from the search  it will give me bellow error Sorry, translation missing: en-GB.type.node #107775...'''
date = "2018-06-08T11:10:00Z"
lastmod = "2018-06-10T20:41:00Z"
weight = 64094
keywords = [ "osm" ]
aliases = [ "/questions/64094" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Search not working in The Rails Port](/questions/64094/search-not-working-in-the-rails-port)

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
<span id="post-64094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64094-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello All, I have installed Rails port , from map point of view its working fine , Navigation works good. only problem is Search is not working, example if i type "City of London" then select one link from the search it will give me bellow error Sorry, translation missing: en-GB.type.node #107775 could not be found.</p>
<p>what does it mean ? and how to fix it ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '18, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb2a94f867841b58214be09992831d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fosiul&#39;s gravatar image" />
<p><span>fosiul</span><br />
<span class="score" title="96 reputation points">96</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fosiul has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-64094" class="comments-container">
&#10;</div>
<div id="comment-tools-64094" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64094-form-container" class="comment-form-container">
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

<span id="64105"></span>

<div id="answer-container-64105" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64105-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fosiul has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You likely don't have any data in the database of the rails-port.</p>
<p>The search itself works because that will go to the OSMF nominatim servers, but because you don't have the data locally your rails port won't be able to display anything.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '18, 16:21</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-64105" class="comments-container">
<span id="64106"></span>
<div id="comment-64106" class="comment">
<div id="post-64106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ahh ok , i think i am understanding,</p>
<p>so if i do search on Ralis-port, it actually goes to nomination server,</p>
<p>so you saying, if i setup a nomination server then the search will work ?</p>
</div>
<div id="comment-64106-info" class="comment-info">
<span class="comment-age">(08 Jun '18, 18:05)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="64108"></span>
<div id="comment-64108" class="comment">
<div id="post-64108-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have a look at 2 pictures it give the search result <a href="https://ibb.co/bW8FYT">https://ibb.co/bW8FYT</a></p>
<p>When i click on any link, it gives you the map but through an errr <a href="https://ibb.co/bNeptT">https://ibb.co/bNeptT</a></p>
<p>so does it mean, I dont have nomination server locally ?</p>
</div>
<div id="comment-64108-info" class="comment-info">
<span class="comment-age">(08 Jun '18, 18:12)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="64109"></span>
<div id="comment-64109" class="comment">
<div id="post-64109-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It would maybe be a good idea to explain what you want to be able to do with the system in the end.</p>
</div>
<div id="comment-64109-info" class="comment-info">
<span class="comment-age">(08 Jun '18, 18:46)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="64114"></span>
<div id="comment-64114" class="comment">
<div id="post-64114-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a> Actually that search is not important to me as I am not going to offer services to people for searching by using our map.</p>
<p>but I am just courious why thats failling and what i can do to fix it thats all. its just bugging me.</p>
</div>
<div id="comment-64114-info" class="comment-info">
<span class="comment-age">(09 Jun '18, 00:57)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="64127"></span>
<div id="comment-64127" class="comment">
<div id="post-64127-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>As already said, the search box on your rails-port instance is using the OSMF nominatim servers, which return found data that isn't in your local API database. The rails-port then tries to display the corresponding element on the map from the local storage which naturally fails because your API database is likely unpopulated (try the same search on openstreetmap.org and you will see what happens).</p>
</div>
<div id="comment-64127-info" class="comment-info">
<span class="comment-age">(09 Jun '18, 10:22)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="64147"></span>
<div id="comment-64147" class="comment not_top_scorer">
<div id="post-64147-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a></p>
</div>
<div id="comment-64147-info" class="comment-info">
<span class="comment-age">(10 Jun '18, 20:41)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
</div>
<div id="comment-tools-64105" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-64105-form-container" class="comment-form-container">
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

