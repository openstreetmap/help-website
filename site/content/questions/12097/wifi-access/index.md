+++
type = "question"
title = "WIFI Access"
description = '''Is there a way to tag a facility offering Wifi, whether it is free, and be able to search on this?'''
date = "2012-04-17T20:36:00Z"
lastmod = "2012-04-18T01:38:00Z"
weight = 12097
keywords = [ "wifi" ]
aliases = [ "/questions/12097" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [WIFI Access](/questions/12097/wifi-access)

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
<span id="post-12097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12097-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to tag a facility offering Wifi, whether it is free, and be able to search on this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Apr '12, 20:36</strong></p>
<img src="https://secure.gravatar.com/avatar/62d8c1450a0d27f08a47c008f3394774?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="azlen&#39;s gravatar image" />
<p><span>azlen</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="azlen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12097" class="comments-container">
&#10;</div>
<div id="comment-tools-12097" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12097-form-container" class="comment-form-container">
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

<span id="12104"></span>

<div id="answer-container-12104" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12104-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to <a href="http://taginfo.openstreetmap.org/keys/wifi#overview">taginfo</a>, there are a couple of thousand uses of wifi=something. Click the tabs on that link and you can see the values used and what other tags it is used with.</p>
<p>To search for this, you can use something like the XAPI or Overpass - see <a href="https://wiki.openstreetmap.org/wiki/Xapi">this</a> wiki page and the links from it. As an example, this command:</p>
<pre><code>wget http://open.mapquestapi.com/xapi/api/0.6/*[wifi=*][bbox=-1.474,52.898,-1.454,52.938]</code></pre>
<p>will search for nodes and ways in part of central England with "wifi" set to something.</p>
<p>(If you're unfamilar with "wget", it's just a command used to get a web page and stick it in a file. It's standard in Unix-like operating systems and available for others)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Apr '12, 00:00</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-12104" class="comments-container">
<span id="12107"></span>
<div id="comment-12107" class="comment">
<div id="post-12107-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note that OpenCycleMap shows pubs marked with wifi, with some 'radiation' coming out of the pint, e.g.:</p>
<p><a href="https://www.openstreetmap.org/?lat=50.78708&amp;lon=-1.0803&amp;zoom=18&amp;layers=C">https://www.openstreetmap.org/?lat=50.78708&amp;lon=-1.0803&amp;zoom=18&amp;layers=C</a></p>
<p>Normally it would be free (for customers).</p>
<p>OCM may show wifi on other places, cafes for example - but I'm not sure.</p>
</div>
<div id="comment-12107-info" class="comment-info">
<span class="comment-age">(18 Apr '12, 00:35)</span> <span class="comment-user userinfo">robbieonsea</span>
</div>
</div>
<span id="12108"></span>
<div id="comment-12108" class="comment">
<div id="post-12108-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The tag <code>internet_access=wlan</code> is also in use for places with wifi (over 4000 uses according to Taginfo). See the wiki page <a href="https://wiki.openstreetmap.org/wiki/Key:internet_access">https://wiki.openstreetmap.org/wiki/Key:internet_access</a></p>
</div>
<div id="comment-12108-info" class="comment-info">
<span class="comment-age">(18 Apr '12, 01:38)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
</div>
<div id="comment-tools-12104" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12104-form-container" class="comment-form-container">
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

