+++
type = "question"
title = "[JOSM] Are parent and child relations related to role=subarea?"
description = '''IMU it is only when relations have members with role=subarea (eg:   considered as &quot;Optional, disputed and redundant&quot; in the wiki, that the child relations tab like   is filled and parent relations tab like    is filled if the relation is itself a member with role=subarea of a parent relation. Am I c...'''
date = "2020-04-15T17:08:00Z"
lastmod = "2020-04-16T17:53:00Z"
weight = 74207
keywords = [ "josm", "role", "tagging", "relations" ]
aliases = [ "/questions/74207" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[JOSM\] Are parent and child relations related to role=subarea?](/questions/74207/josm-are-parent-and-child-relations-related-to-rolesubarea)

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
<span id="post-74207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74207-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>IMU it is only when relations have members with role=subarea (eg:</p>
<p><embed src="https://leslibresgeographes.org/jirafeau/f.php?h=1-25sVe0&amp;p=1" /></p>
<p>considered as "Optional, disputed and redundant" in the <a href="https://wiki.openstreetmap.org/wiki/Relation:boundary#Relation_members">wiki</a>, that the child relations tab like</p>
<p><embed src="https://leslibresgeographes.org/jirafeau/f.php?h=2OFMXbUI&amp;p=1" /></p>
<p>is filled and parent relations tab like</p>
<p><embed src="https://leslibresgeographes.org/jirafeau/f.php?h=0Y5oGI2M&amp;p=1" /></p>
<p>is filled if the relation is itself a member with role=subarea of a parent relation. Am I correct?</p>
<p>If so, as the use of this role is not recommended yet, we should expect no information in those tabs for administrative=boundary relations?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-role" rel="tag" title="see questions tagged &#39;role&#39;">role</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '20, 17:08</strong></p>
<img src="https://secure.gravatar.com/avatar/35a2e88e2106806c0ba99b9b5e6ef093?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SeverinGeo&#39;s gravatar image" />
<p><span>SeverinGeo</span><br />
<span class="score" title="81 reputation points">81</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SeverinGeo has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-74207" class="comments-container">
&#10;</div>
<div id="comment-tools-74207" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74207-form-container" class="comment-form-container">
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

<span id="74228"></span>

<div id="answer-container-74228" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74228-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, you are correct. And it's true that you shouldn't expect any info in those tabs if the relation don't have any relations as members.</p>
<p>I guess the wiki should clarify this when it talks about the subarea role.</p>
<p>One clarification in general: a relation P will have X children relations if it has that same X number of relations as members, independently of the role type of each of those members (or even if those members have a void role). And each of those relations will have as a parent the relation P.</p>
<p>For example:</p>
<pre><code>&lt;?xml version=&#39;1.0&#39; encoding=&#39;UTF-8&#39;?&gt; &lt;osm version=&#39;0.6&#39; generator=&#39;JOSM&#39;&gt;
&lt;relation id=&#39;-1&#39; action=&#39;modify&#39; visible=&#39;true&#39;&gt;
    &lt;tag k=&#39;type&#39; v=&#39;typea&#39; /&gt;
    &lt;tag k=&#39;name&#39; v=&#39;Child relation A&#39; /&gt;
&lt;/relation&gt;
&lt;relation id=&#39;-2&#39; action=&#39;modify&#39; visible=&#39;true&#39;&gt;
    &lt;tag k=&#39;type&#39; v=&#39;typeb&#39; /&gt;
    &lt;tag k=&#39;name&#39; v=&#39;Child relation A&#39; /&gt;
&lt;/relation&gt;
&lt;relation id=&#39;-3&#39; action=&#39;modify&#39; visible=&#39;true&#39;&gt;
    &lt;member type=&#39;relation&#39; ref=&#39;-1&#39; role=&#39;rolea&#39; /&gt;
    &lt;member type=&#39;relation&#39; ref=&#39;-2&#39; role=&#39;&#39; /&gt;
    &lt;tag k=&#39;type&#39; v=&#39;typec&#39; /&gt;
    &lt;tag k=&#39;name&#39; v=&#39;I am parent of the relations A and B&#39; /&gt;
&lt;/relation&gt;
&lt;/osm&gt;</code></pre>
<p>The last relation is parent of the first 2 relations. And each of those 2 relations have as parent the last relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '20, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/d45c161edd4b471fd947a7ec574274ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edvac&#39;s gravatar image" />
<p><span>edvac</span><br />
<span class="score" title="665 reputation points">665</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edvac has 4 accepted answers">15%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Apr '20, 17:56</strong> </span></p>
</div>
</div>
<div id="comments-container-74228" class="comments-container">
&#10;</div>
<div id="comment-tools-74228" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74228-form-container" class="comment-form-container">
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

