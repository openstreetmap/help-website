+++
type = "question"
title = "Function &quot;length&quot; not known ?"
description = '''Hi - being new to overpass Turbo, I have found several examples of the use of the length() function.  But it seems not to be working any longer - running this small example gives an error [out:json][timeout:25]; (  way[&quot;highway&quot;] ({{bbox}});  ); make stat number=count(ways),length=sum(length()); out...'''
date = "2022-01-08T10:55:00Z"
lastmod = "2022-01-09T13:08:00Z"
weight = 83000
keywords = [ "length", "overpass-turbo" ]
aliases = [ "/questions/83000" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Function "length" not known ?](/questions/83000/function-length-not-known)

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
<span id="post-83000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83000-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi - being new to overpass Turbo, I have found several examples of the use of the length() function.</p>
<p>But it seems not to be working any longer - running this small example gives an error</p>
<pre><code>[out:json][timeout:25];
(
  way[&quot;highway&quot;]  ({{bbox}});                                                                                                                                        
);
make stat number=count(ways),length=sum(length());
out body;
&gt;;
out skel qt;</code></pre>
<p>So how do I get a total road length?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jan '22, 10:55</strong></p>
<img src="https://secure.gravatar.com/avatar/6c0e89d2435469a3328c23874fb9d9d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jenspeterhansen&#39;s gravatar image" />
<p><span>jenspeterhansen</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jenspeterhansen has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jan '22, 20:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-83000" class="comments-container">
&#10;</div>
<div id="comment-tools-83000" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83000-form-container" class="comment-form-container">
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

<span id="83001"></span>

<div id="answer-container-83001" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83001-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>you should use the "code" formatting, or the Share function of overpass-turbo, as this website scramble the query otherwise.</p>
<p>Anyway, if I try it, it seems to work alright : <a href="http://overpass-turbo.eu/s/1eVq">http://overpass-turbo.eu/s/1eVq</a></p>
<p>It is not an error if you get no displayable data, overpass-turbo is meant to display geographic data, on top of the map. But here you get only numbers, which seems right, just check in the data panel.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '22, 12:32</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-83001" class="comments-container">
&#10;</div>
<div id="comment-tools-83001" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83001-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83007"></span>

<div id="answer-container-83007" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83007-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi H_mlet - thanks for responding.</p>
<p>After comparing your example (working) letter by letter with my own example (error message), I found out, that changing from using the server //overpass.openstreetmap.fr/api/ to //overpass-api.de/api/ solved my problem. :-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '22, 19:56</strong></p>
<img src="https://secure.gravatar.com/avatar/6c0e89d2435469a3328c23874fb9d9d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jenspeterhansen&#39;s gravatar image" />
<p><span>jenspeterhansen</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jenspeterhansen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83007" class="comments-container">
<span id="83024"></span>
<div id="comment-83024" class="comment">
<div id="post-83024-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Tricky one. I guess OSMFR doesn't have the time to update their overpass instance... Glad you found the problem. Regards.</p>
</div>
<div id="comment-83024-info" class="comment-info">
<span class="comment-age">(09 Jan '22, 13:08)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-83007" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83007-form-container" class="comment-form-container">
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

