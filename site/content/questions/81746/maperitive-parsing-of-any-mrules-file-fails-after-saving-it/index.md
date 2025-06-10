+++
type = "question"
title = "Maperitive: parsing of any mrules file fails after saving it"
description = '''In Maperitive I have a strange problem, that seems to make any reloading of mrules files impossible: steps to reproduce: I am running Maperitive v2.4.3 on mono 6.12.0 on Arch Linux.  launch Maperitive load random area from overpass api go to Map-&amp;gt;&quot;Edit rendering rules&quot;, which fires up gvim on my ...'''
date = "2021-09-14T21:18:00Z"
lastmod = "2021-09-14T21:18:00Z"
weight = 81746
keywords = [ "maperitive", "mrules" ]
aliases = [ "/questions/81746" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Maperitive: parsing of any mrules file fails after saving it](/questions/81746/maperitive-parsing-of-any-mrules-file-fails-after-saving-it)

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
<span id="post-81746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81746-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In Maperitive I have a strange problem, that seems to make any reloading of mrules files impossible:</p>
<p>steps to reproduce:</p>
<p>I am running Maperitive v2.4.3 on mono 6.12.0 on Arch Linux.</p>
<ul>
<li>launch Maperitive</li>
<li>load random area from overpass api</li>
<li>go to Map-&gt;"Edit rendering rules", which fires up gvim on my system</li>
<li>save the unchanged file in the editor</li>
</ul>
<p>Reloading the mrules file fails with the following errors:</p>
<pre><code>ERROR: Unexpected token &#39;VALUE&#39; (line=14, col=15)
ERROR: Unexpected token &#39;VALUE&#39; (line=12, col=13)
ERROR: Wrong indentation (line=15, col=3)
ERROR: Wrong indentation (line=16, col=3)
...</code></pre>
<p>The rules file is the "Default.mrules". At first I thought, my vim would automatically replace some whitespace on saving, but that seems not to be the case. I downloaded the original versions of the files again and initialized a git repository in the "Rules" directory, to monitor any changes, which doesn't show me any changes after saving the file again. Most strangely, restarting Maperitive and loading the mrules file again fixes the problem, until I am saving the mrules file again.</p>
<p>I am totally clueless about this. It is quite a major blocker in the workflow, since Maperitive has to be restarted after every change to the rules file, so that parsing it works again.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span> <span class="post-tag tag-link-mrules" rel="tag" title="see questions tagged &#39;mrules&#39;">mrules</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '21, 21:18</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd1b8ea867dced3458ac02365ba5936?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="farad&#39;s gravatar image" />
<p><span>farad</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="farad has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Sep '21, 17:13</strong> </span></p>
</div>
</div>
<div id="comments-container-81746" class="comments-container">
&#10;</div>
<div id="comment-tools-81746" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81746-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

