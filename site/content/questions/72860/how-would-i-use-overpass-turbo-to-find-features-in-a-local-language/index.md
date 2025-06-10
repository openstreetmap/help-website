+++
type = "question"
title = "How would I use Overpass-turbo to find features in a local language?"
description = '''I&#x27;m hoping to create a map that is in Tlingit, the language of the people who first occupied my local area (see this site). Some features have a name:tli tag. Area in question How could I query the features that have that tag? I tried [name:tli is NOT NULL] and it didn&#x27;t work.'''
date = "2020-02-05T01:16:00Z"
lastmod = "2020-02-06T15:41:00Z"
weight = 72860
keywords = [ "query", "overpass-turbo" ]
aliases = [ "/questions/72860" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How would I use Overpass-turbo to find features in a local language?](/questions/72860/how-would-i-use-overpass-turbo-to-find-features-in-a-local-language)

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
<span id="post-72860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72860-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm hoping to create a map that is in Tlingit, the language of the people who first occupied my local area (see <a href="https://native-land.ca/maps/territories/tlingit/">this site</a>). Some features have a name:tli tag. <a href="https://www.openstreetmap.org/#map=15/57.0522/-135.3325">Area in question</a> How could I query the features that have that tag? I tried [name:tli is NOT NULL] and it didn't work.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '20, 01:16</strong></p>
<img src="https://secure.gravatar.com/avatar/efa2bd232d1bfd0540fe303e6cba5f64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jfact0ry&#39;s gravatar image" />
<p><span>Jfact0ry</span><br />
<span class="score" title="366 reputation points">366</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jfact0ry has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Feb '20, 01:17</strong> </span></p>
</div>
</div>
<div id="comments-container-72860" class="comments-container">
&#10;</div>
<div id="comment-tools-72860" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72860-form-container" class="comment-form-container">
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

<span id="72862"></span>

<div id="answer-container-72862" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72862-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-72862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jfact0ry has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To query for a key without considering the values, put the key in the brackets, here using quotes because of the colon in the key:</p>
<p><a href="http://overpass-turbo.eu/s/QoK"><code>nwr["name:tli"];</code></a>.</p>
<p>There aren't many features with that tag:</p>
<p><a href="https://taginfo.openstreetmap.org/keys/name%3Atli">https://taginfo.openstreetmap.org/keys/name%3Atli</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '20, 02:17</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-72862" class="comments-container">
<span id="72875"></span>
<div id="comment-72875" class="comment">
<div id="post-72875-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! Yes, the goal is to show it's possible and then get more of the landmarks in local language mapped. Gunalchéesh!</p>
</div>
<div id="comment-72875-info" class="comment-info">
<span class="comment-age">(05 Feb '20, 19:01)</span> <span class="comment-user userinfo">Jfact0ry</span>
</div>
</div>
<span id="72896"></span>
<div id="comment-72896" class="comment">
<div id="post-72896-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/7398/jfact0ry"></a><a href="https://help.openstreetmap.org/users/7398/jfact0ry">@Jfact0ry</a> You can use for example <code>node[place][!"lang:tli"]({{bbox}});</code> to query for <code>place=*</code> features without a name your language, using the <code>!</code> not operator. Be careful not to make the box too wide in area to avoid over-limit.</p>
</div>
<div id="comment-72896-info" class="comment-info">
<span class="comment-age">(06 Feb '20, 15:41)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-72862" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72862-form-container" class="comment-form-container">
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

