+++
type = "question"
title = "[Xapi] node has wrong coordinates"
description = '''Hi, When I look on www.openstreetmap.org/node/30658698, the node coordinates are Location: 36.7762244, -2.0629709 But when I get the node through xapi, I receive this:   &amp;lt;node id=&quot;30658698&quot; lat=&quot;36.7763260&quot; lon=&quot;-2.0624340&quot; version=&quot;1&quot; timestamp=&quot;2007-06-20T00:31:08Z&quot; changeset=&quot;104149&quot; uid=&quot;4623...'''
date = "2015-02-04T09:12:00Z"
lastmod = "2015-02-04T11:05:00Z"
weight = 40766
keywords = [ "node", "xapi", "coordinates" ]
aliases = [ "/questions/40766" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[Xapi\] node has wrong coordinates](/questions/40766/xapi-node-has-wrong-coordinates)

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
<span id="post-40766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40766-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>When I look on www.openstreetmap.org/node/30658698, the node coordinates are Location: 36.7762244, -2.0629709</p>
<p>But when I get the node through xapi, I receive this: <code> &lt;node id="30658698" lat="36.7763260" lon="-2.0624340" version="1" timestamp="2007-06-20T00:31:08Z" changeset="104149" uid="4623" user="Quico"&gt; &lt;tag k="created_by" v="almien_coastlines mod"/&gt; &lt;tag k="source" v="PGS"/&gt; &lt;/node&gt; </code></p>
<p>The coordinates are different and it results in a self-crossing way...</p>
<p>Any ideas why ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '15, 09:12</strong></p>
<img src="https://secure.gravatar.com/avatar/e826d17bc44218dd45c0a7fec0dec7da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sallesma&#39;s gravatar image" />
<p><span>sallesma</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sallesma has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40766" class="comments-container">
<span id="40767"></span>
<div id="comment-40767" class="comment">
<div id="post-40767-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which XAPI were you using? Whichever one it was I suspect that it has not been updated in at least 10 months!</p>
</div>
<div id="comment-40767-info" class="comment-info">
<span class="comment-age">(04 Feb '15, 09:24)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="40768"></span>
<div id="comment-40768" class="comment">
<div id="post-40768-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I use <a href="http://api.openstreetmap.fr/xapi">http://api.openstreetmap.fr/xapi</a></p>
<p>Information on the wiki (<a href="http://wiki.openstreetmap.org/wiki/Servers/api.openstreetmap.fr#Data_a_little_older)">http://wiki.openstreetmap.org/wiki/Servers/api.openstreetmap.fr#Data_a_little_older)</a> says that it can be "1 or 2 minutes late"</p>
</div>
<div id="comment-40768-info" class="comment-info">
<span class="comment-age">(04 Feb '15, 09:45)</span> <span class="comment-user userinfo">sallesma</span>
</div>
</div>
</div>
<div id="comment-tools-40766" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40766-form-container" class="comment-form-container">
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

<span id="40769"></span>

<div id="answer-container-40769" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40769-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sallesma has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'll need to raise the problem with whoever looks after <a href="http://api.openstreetmap.fr/xapi">http://api.openstreetmap.fr/xapi</a> (I had no idea that it even existed).</p>
<p>Try one of the other options at <a href="http://wiki.openstreetmap.org/wiki/Xapi">http://wiki.openstreetmap.org/wiki/Xapi</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '15, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-40769" class="comments-container">
<span id="40770"></span>
<div id="comment-40770" class="comment">
<div id="post-40770-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your help</p>
</div>
<div id="comment-40770-info" class="comment-info">
<span class="comment-age">(04 Feb '15, 10:50)</span> <span class="comment-user userinfo">sallesma</span>
</div>
</div>
<span id="40771"></span>
<div id="comment-40771" class="comment">
<div id="post-40771-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If anyone has the same problem: The way containing this node is marked with timestamp="2014-10-24T22:10:42Z" which would mean that the way is up to date but not its nodes... Interesting</p>
</div>
<div id="comment-40771-info" class="comment-info">
<span class="comment-age">(04 Feb '15, 11:05)</span> <span class="comment-user userinfo">sallesma</span>
</div>
</div>
</div>
<div id="comment-tools-40769" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40769-form-container" class="comment-form-container">
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

