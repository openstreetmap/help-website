+++
type = "question"
title = "Is it possible to get my 20 most recent edits using Overpass Turbo?"
description = '''I&#x27;m trying to get my 20 most recent edits and export it as a JSON, but I can&#x27;t seem to get overpass to limit my query properly. This is my query: [out:json][timeout:60]; (  node(user:&quot;bddavidson&quot;)({{bbox}});  way(user:&quot;bddavidson&quot;)({{bbox}});  relation(user:&quot;bddavidson&quot;)({{bbox}}); ); // print resul...'''
date = "2017-05-01T16:14:00Z"
lastmod = "2017-05-01T17:23:00Z"
weight = 55974
keywords = [ "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/55974" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to get my 20 most recent edits using Overpass Turbo?](/questions/55974/is-it-possible-to-get-my-20-most-recent-edits-using-overpass-turbo)

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
<span id="post-55974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55974-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to get my 20 most recent edits and export it as a JSON, but I can't seem to get overpass to limit my query properly. This is my query:</p>
<pre><code>[out:json][timeout:60];
(
  node(user:&quot;bddavidson&quot;)({{bbox}});
  way(user:&quot;bddavidson&quot;)({{bbox}});
  relation(user:&quot;bddavidson&quot;)({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>I've tried using the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Print_.28out.29">print actions found here</a> to limit on the <code>out</code> commands, but I haven't had any luck so far. I also tried on the <code>&gt;</code>, but that didn't seem to work either.</p>
<p>Is there currently a way with Overpass to get my 20 most recent changes no matter what they are (point/line/polygon)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 May '17, 16:14</strong></p>
<img src="https://secure.gravatar.com/avatar/c37cbe38f485579bcc6a040b405b55e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bddavidson&#39;s gravatar image" />
<p><span>bddavidson</span><br />
<span class="score" title="161 reputation points">161</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bddavidson has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 May '17, 16:14</strong> </span></p>
</div>
</div>
<div id="comments-container-55974" class="comments-container">
<span id="55975"></span>
<div id="comment-55975" class="comment">
<div id="post-55975-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think you'll have to manually determine the date of the 20th changeset back and then use <code>newer</code> or <code>diff</code> to fetch the changes since that time.</p>
</div>
<div id="comment-55975-info" class="comment-info">
<span class="comment-age">(01 May '17, 17:23)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-55974" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55974-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

