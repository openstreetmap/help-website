+++
type = "question"
title = "Strange FIND function result"
description = '''Hi All, Please try to find place by location like: &quot; 50.31235 34.86754&quot; (with space before the numbers), next you will try to find for: &quot;50.31235 34.86754&quot;. I have completely different places result.. The first of requests return (in Russian lang.) &quot;Т-17-05, Кнышовка, Гадячский район, Полтавская обл...'''
date = "2012-12-28T11:58:00Z"
lastmod = "2013-01-02T15:11:00Z"
weight = 18741
keywords = [ "interface", "web", "bugs", "find" ]
aliases = [ "/questions/18741" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Strange FIND function result](/questions/18741/strange-find-function-result)

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
<span id="post-18741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18741-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>Please try to find place by location like: " 50.31235 34.86754" (with space before the numbers), next you will try to find for: "50.31235 34.86754".</p>
<p>I have completely different places result..</p>
<p>The first of requests return (in Russian lang.) "Т-17-05, Кнышовка, Гадячский район, Полтавская область, Украина" and point to road in the forest - wrong place! Next request return no text but point to true geographic location (Ohtyrka town).</p>
<p>Hot I can to fix it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-web" rel="tag" title="see questions tagged &#39;web&#39;">web</span> <span class="post-tag tag-link-bugs" rel="tag" title="see questions tagged &#39;bugs&#39;">bugs</span> <span class="post-tag tag-link-find" rel="tag" title="see questions tagged &#39;find&#39;">find</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Dec '12, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/8c20a04518a8aa539a51e5fd237c4546?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VladUA&#39;s gravatar image" />
<p><span>VladUA</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VladUA has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18741" class="comments-container">
<span id="18742"></span>
<div id="comment-18742" class="comment">
<div id="post-18742-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>They're not quite "completely different places" - they're both on the same road.</p>
</div>
<div id="comment-18742-info" class="comment-info">
<span class="comment-age">(28 Dec '12, 12:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="18823"></span>
<div id="comment-18823" class="comment">
<div id="post-18823-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, but search result is very differ :) I will try to explain.</p>
<p>Right point place located near the building inside the neighborhood 30m from the T-17-05 inside the "Ohtyrka" town. In search result we find another region (oblast) address - near 50 km from place point by geo location.</p>
<p>I expect to get nearest town address but not a road name with address of center this road.</p>
</div>
<div id="comment-18823-info" class="comment-info">
<span class="comment-age">(02 Jan '13, 15:11)</span> <span class="comment-user userinfo">VladUA</span>
</div>
</div>
</div>
<div id="comment-tools-18741" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18741-form-container" class="comment-form-container">
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

<span id="18743"></span>

<div id="answer-container-18743" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18743-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-18743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When you use the "Search" box on openstreetmap.org, it uses several different services.</p>
<p>If what you type in is recognised as coordinates, then the "Internal" service will give you a link directly to that point.</p>
<p>If your input is not recognised as coordinates, it will search Nominatim and GeoNames. These are designed for finding placenames and addresses. It seems Nominatim will give you the nearest road or address to the coordinates, which might be some distance away.</p>
<p>The problem is that the internal service only recognises coordinates if they are formatted in a particular way. ie only if they are decimal degrees. So as you've found, it doesn't work if they have extra spaces, or N/S, or degrees/minutes/seconds etc.</p>
<p>You could report this by adding a ticket on <a href="https://trac.openstreetmap.org/">https://trac.openstreetmap.org/</a> It may have been reported previously, so try searching first.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Dec '12, 17:19</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-18743" class="comments-container">
<span id="18822"></span>
<div id="comment-18822" class="comment">
<div id="post-18822-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the response!</p>
<p>But trailing/leading spaces do not affect to the numbers inside the request. So we have trivial bug in request processor or not?</p>
<p>Ok, I try to make new ticket.</p>
</div>
<div id="comment-18822-info" class="comment-info">
<span class="comment-age">(02 Jan '13, 14:53)</span> <span class="comment-user userinfo">VladUA</span>
</div>
</div>
</div>
<div id="comment-tools-18743" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18743-form-container" class="comment-form-container">
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

