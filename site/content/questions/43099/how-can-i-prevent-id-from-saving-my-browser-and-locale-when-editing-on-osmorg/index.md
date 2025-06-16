+++
type = "question"
title = "How can i prevent iD from saving my Browser and locale when editing on osm.org?"
description = '''As you can see on this image:  ... the iD Editor saves a bunch of questionable data by default.  Is there a way to prevent this behaviour?'''
date = "2015-05-17T22:36:00Z"
lastmod = "2015-05-19T03:05:00Z"
weight = 43099
keywords = [ "ideditor", "privacy" ]
aliases = [ "/questions/43099" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can i prevent iD from saving my Browser and locale when editing on osm.org?](/questions/43099/how-can-i-prevent-id-from-saving-my-browser-and-locale-when-editing-on-osmorg)

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
<span id="post-43099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43099-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As you can see on this image:</p>
<p><img src="//i.imgur.com/ut4CDE3.png" alt="changeset with personal data" /></p>
<p>... the iD Editor saves a bunch of questionable data by default. Is there a way to prevent this behaviour?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-privacy" rel="tag" title="see questions tagged &#39;privacy&#39;">privacy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 May '15, 22:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0aa579d80c18a1086fdf2425905d41a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="redplanet&#39;s gravatar image" />
<p><span>redplanet</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="redplanet has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 May '15, 21:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-43099" class="comments-container">
&#10;</div>
<div id="comment-tools-43099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43099-form-container" class="comment-form-container">
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

<span id="43101"></span>

<div id="answer-container-43101" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43101-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43101-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-43101-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>FWIW, we have already removed this behavior from master.. So you can just use the iD that is hosted on <a href="http://openstreetmap.us/iD/master/">http://openstreetmap.us/iD/master/</a> and it will not write these things into the changeset.</p>
<p>There is another option too: What's nice about iD is that it is a JavaScript app and so you can change almost anything about it that you do not like, while it is running. Pretty awesome huh? Here's how:</p>
<p>1) Open Developer Tools and find the console</p>
<p>2) (if you are on openstreetmap.org) make sure the console is debugging the iD iframe:</p>
<p>in Chrome/Safari: change the dropdown from <code>&lt;top frame&gt;</code> to <code>id-embed (id)</code></p>
<p>in Firefox: type <code>cd('#id-embed')</code></p>
<p>3) Enter commands to remove the things you don't like:</p>
<p><code>iD.detect().browser = ''</code></p>
<p><code>iD.detect().version = ''</code></p>
<p><code>iD detect().platform = ''</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 May '15, 02:48</strong></p>
<img src="https://secure.gravatar.com/avatar/5372740989fdca18458f194a285fcb3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhousel&#39;s gravatar image" />
<p><span>bhousel</span><br />
<span class="score" title="2089 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhousel has 13 accepted answers">38%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 May '15, 02:51</strong> </span></p>
</div>
</div>
<div id="comments-container-43101" class="comments-container">
<span id="43107"></span>
<div id="comment-43107" class="comment">
<div id="post-43107-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>… and <a href="http://openstreetmap.us/iD/master/">http://openstreetmap.us/iD/master/</a> uses google analytics to spy on the user and share the user's data with google … "pretty awesome" too. ;-)</p>
<p>Thanks for the description of the theoretical possibility to do a live patch of iD, though! But you will agree that barely no OSM will practically do this for each iD session.</p>
<p>a link to the relevant change ("we have already removed this behavior"): <a href="https://github.com/openstreetmap/iD/pull/2643">https://github.com/openstreetmap/iD/pull/2643</a></p>
</div>
<div id="comment-43107-info" class="comment-info">
<span class="comment-age">(18 May '15, 21:45)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="43108"></span>
<div id="comment-43108" class="comment">
<div id="post-43108-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Whoa, aseerel4c26. bhousel posts that the iD developers have already changed this - i.e. it's just waiting for the next osm.org deployment to update it - and you still take the opportunity to flame him. Great way to encourage developers to contribute to osm.org.</p>
</div>
<div id="comment-43108-info" class="comment-info">
<span class="comment-age">(18 May '15, 23:23)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="43109"></span>
<div id="comment-43109" class="comment">
<div id="post-43109-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5/richard"></a><a href="https://help.openstreetmap.org/users/5/richard">@Richard</a>: yes, this issue is whoa indeed. To make my comment less whoa I have removed the side question which I answered myself (the link).</p>
<p>Yes, it is nice that the issue is partly resolved now (I already had added a "Update" section to <span>my diary entry about this</span>). Note that the OP <a href="https://help.openstreetmap.org/users/10995/redplanet"></a><a href="https://help.openstreetmap.org/users/10995/redplanet">@redplanet</a> complains about his "locale" in the title and <a href="https://help.openstreetmap.org/users/7499/bhousel"></a><a href="https://help.openstreetmap.org/users/7499/bhousel">@bhousel</a> reports that the new version "will not write these things into the changeset". Not true – if I see correctly in the github pull/merge the locale is still silently saved into the changeset.</p>
<p>Regarding your ironic last sentence: Please tell me, why should I want to encourage developers doing changes to OSM software which more or less irreversibly invade the privacy of thousands of OSM contributors and cost a big amount of all of our time? I did not even read (I may have missed it) an excuse ... Yes, I think I know where you are coming from – we need more devs doing good work, I fully agree. But needing devs does not mean that they are king and that ordinary OSM contributors have no rights.</p>
</div>
<div id="comment-43109-info" class="comment-info">
<span class="comment-age">(19 May '15, 00:37)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="43110"></span>
<div id="comment-43110" class="comment">
<div id="post-43110-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>Thanks for the description of the theoretical possibility to do a live patch of iD, though! But you will agree that barely no one on OSM will practically do this for each iD session.</p>
</blockquote>
<p>Oh definitely. I think it's far more likely that anyone that concerned about concealing which browser they use would just spoof their UserAgent string.</p>
</div>
<div id="comment-43110-info" class="comment-info">
<span class="comment-age">(19 May '15, 03:05)</span> <span class="comment-user userinfo">bhousel</span>
</div>
</div>
</div>
<div id="comment-tools-43101" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43101-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43100"></span>

<div id="answer-container-43100" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43100-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-43100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Id is an open source editor so there certainly is a way to prevent this behaviour - download the source, modify the bit you don't like, and run your own version. You can even offer this modified version to other users concerned about privacy like you are.</p>
<p>If you want to file an issue with the Id editor, see <a href="https://github.com/openstreetmap/iD/issues">https://github.com/openstreetmap/iD/issues</a> ; you might also want to read <a href="https://www.openstreetmap.org/user/aseerel4c26/diary/34899">https://www.openstreetmap.org/user/aseerel4c26/diary/34899</a> for a discussion about the matter.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '15, 23:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-43100" class="comments-container">
&#10;</div>
<div id="comment-tools-43100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43100-form-container" class="comment-form-container">
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

