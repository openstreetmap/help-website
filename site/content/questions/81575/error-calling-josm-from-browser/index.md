+++
type = "question"
title = "error calling JOSM from browser"
description = '''Hi everyone. For a few weeks or so I have encountered a problem when clicking on the edit button on www.openstreetmap.org.  As set in my user preferences the edit request is passed to JOSM and JOSM downloads the data as it should. Nevertheless, if the data quantity is on the larger side I always get...'''
date = "2021-08-31T14:56:00Z"
lastmod = "2021-08-31T16:19:00Z"
weight = 81575
keywords = [ "josm", "josm_remote_control" ]
aliases = [ "/questions/81575" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [error calling JOSM from browser](/questions/81575/error-calling-josm-from-browser)

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
<span id="post-81575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81575-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone. For a few weeks or so I have encountered a problem when clicking on the edit button on www.openstreetmap.org.</p>
<p>As set in my user preferences the edit request is passed to JOSM and JOSM downloads the data as it should. Nevertheless, if the data quantity is on the larger side I always get a pop-up on the website telling me that JOSM could not be started. It is the same error message that appears when JOSM is not running. If the data quantity is smaller this does not happen. Without me knowing what communication is going on between the browser and JOSM it appears to me that JOSM only acknowledges the download request once the data has been downloaded completely. If that download takes a bit longer the browser quits waiting and issues the error message.</p>
<p>I don't recall this has ever happened before. It happens with Opera and with Firefox and JOSM 18004 (and I believe some earlier version, I update irregularly)</p>
<p>Any hints what I might need to change in either application?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-josm_remote_control" rel="tag" title="see questions tagged &#39;josm_remote_control&#39;">josm_remote_control</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '21, 14:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-81575" class="comments-container">
<span id="81576"></span>
<div id="comment-81576" class="comment">
<div id="post-81576-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know what's causing that behaviour but I often see the same error message. The data downloads to JOSM okay so I've just ignored reporting it. I always run the latest version of JOSM (currently v.18118) but it's happened with several older versions as well.</p>
</div>
<div id="comment-81576-info" class="comment-info">
<span class="comment-age">(31 Aug '21, 15:06)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="81577"></span>
<div id="comment-81577" class="comment">
<div id="post-81577-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you mean "Editing failed - make sure JOSM or Merkaartor is loaded and that the remote control option is enabled" then I've had that for ages using Opera and Windows 10 using the dropdown "Edit with Remote Control" option rather than my current default (iD). Not always - if I have a data layer already open in JOSM and add only a small bit to it, things seem OK, so figure there is some low response timeout I very rarely beat.</p>
</div>
<div id="comment-81577-info" class="comment-info">
<span class="comment-age">(31 Aug '21, 15:08)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="81578"></span>
<div id="comment-81578" class="comment">
<div id="post-81578-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I see the same in Potlatch3 and have similarly ignored it, because the invoking of the editor in the right place seems to work.</p>
</div>
<div id="comment-81578-info" class="comment-info">
<span class="comment-age">(31 Aug '21, 15:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="81582"></span>
<div id="comment-81582" class="comment">
<div id="post-81582-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's the message EdLoach.</p>
<p>So I'm not alone. Strange that I have never seen that before until recently.</p>
</div>
<div id="comment-81582-info" class="comment-info">
<span class="comment-age">(31 Aug '21, 16:19)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-81575" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81575-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

