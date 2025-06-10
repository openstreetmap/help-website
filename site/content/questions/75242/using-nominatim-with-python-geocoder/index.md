+++
type = "question"
title = "using nominatim with python geocoder"
description = '''Hi, I&#x27;ve set up Nominatim on an Ubuntu server using the installation documentation. However, it is unclear to me how I actually access this server to geocode. For example, if I wanted to use the python geocoder package (https://geocoder.readthedocs.io/providers/OpenStreetMap.html), how do I actually...'''
date = "2020-06-09T15:32:00Z"
lastmod = "2020-06-12T14:25:00Z"
weight = 75242
keywords = [ "url", "python", "nominatim" ]
aliases = [ "/questions/75242" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [using nominatim with python geocoder](/questions/75242/using-nominatim-with-python-geocoder)

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
<span id="post-75242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75242-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've set up Nominatim on an Ubuntu server using the installation documentation. However, it is unclear to me how I actually access this server to geocode. For example, if I wanted to use the python geocoder package (<a href="https://geocoder.readthedocs.io/providers/OpenStreetMap.html),">https://geocoder.readthedocs.io/providers/OpenStreetMap.html),</a> how do I actually access my version of Nominatim? As in, what is the URL I should be directing my search towards? Any help or guideance would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jun '20, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/3a3e3af440ad8ed5385f87e1957d1642?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bsilver&#39;s gravatar image" />
<p><span>bsilver</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bsilver has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75242" class="comments-container">
&#10;</div>
<div id="comment-tools-75242" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75242-form-container" class="comment-form-container">
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

<span id="75243"></span>

<div id="answer-container-75243" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75243-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-75243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It depends a bit how the webserver got setup. With <a href="http://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-20/#setting-up-the-apache-webserver">http://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-20/#setting-up-the-apache-webserver</a> it's likely</p>
<p><a href="http://server-ip-address/nominatim/search.php">http://server-ip-address/nominatim/search.php</a></p>
<p>and you should be able to open that in a browser. For the python module it should be</p>
<p><a href="http://server-ip-address/nominatim/">http://server-ip-address/nominatim/</a></p>
<p>because it adds /search.php or /reverse.php itself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jun '20, 15:38</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-75243" class="comments-container">
<span id="75244"></span>
<div id="comment-75244" class="comment">
<div id="post-75244-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for this clear answer. The browser address does load a very simple page.</p>
<p>Doing 'http://[server-ip]/nominatim' gets me the same "url does not exist" error that I'd been getting. However, when I add 'search.php' to the end of it, I get a "500 server error," but I'm not sure what could be going wrong. Any ideas of a common reason for this problem?</p>
</div>
<div id="comment-75244-info" class="comment-info">
<span class="comment-age">(09 Jun '20, 16:50)</span> <span class="comment-user userinfo">bsilver</span>
</div>
</div>
<span id="75245"></span>
<div id="comment-75245" class="comment">
<div id="post-75245-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The webserver logfile should show the full error. On Ubuntu look into /var/log/apache2/error.log There is also http://[server-ip]/nominatim/status.php which might have pointers and the <code>cd build; ./utils/check_nominatim_finished.php</code> script.</p>
</div>
<div id="comment-75245-info" class="comment-info">
<span class="comment-age">(09 Jun '20, 16:52)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="75246"></span>
<div id="comment-75246" class="comment">
<div id="post-75246-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, so the error.log file says "Symbolic link not allowed or link target not accessible" and the status.php page says Database query failed. I also don't see a check_nominatim_finished script in utils... But I'm pretty sure Nominatim installed correctly and the map extract I used (just north america) finished importing</p>
</div>
<div id="comment-75246-info" class="comment-info">
<span class="comment-age">(09 Jun '20, 19:01)</span> <span class="comment-user userinfo">bsilver</span>
</div>
</div>
<span id="75248"></span>
<div id="comment-75248" class="comment">
<div id="post-75248-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I mixed up the name, it's <code>check_import_finished.php</code>. It's only a couple of months old, maybe you installed an older version. In your Apache configuration <code>/etc/apache2/conf-available/nominatim.conf</code> look for the <code>&lt;Directory</code> and <code>alias</code> lines and check if those paths exist. Maybe a simple typo.</p>
</div>
<div id="comment-75248-info" class="comment-info">
<span class="comment-age">(09 Jun '20, 19:05)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="75249"></span>
<div id="comment-75249" class="comment">
<div id="post-75249-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh strange, that file isn't there either, so I must have installed an older version (although I started this process last week). I'd been playing around with the nominatim.conf file earlier - the director line is "/srv/nominatim/build/website" and the alias line is the same with the alias as /nominatim. Seems correct? (/srv/nominatim is where my build directory is)</p>
<p>Thanks for your help with this - I feel like I'm really close!</p>
</div>
<div id="comment-75249-info" class="comment-info">
<span class="comment-age">(09 Jun '20, 19:18)</span> <span class="comment-user userinfo">bsilver</span>
</div>
</div>
<span id="75250"></span>
<div id="comment-75250" class="comment not_top_scorer">
<div id="post-75250-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks alright. I have mine in <code>/srv/nominatim/Nominatim/build/website</code> but that depends on which installation instructions you used.</p>
</div>
<div id="comment-75250-info" class="comment-info">
<span class="comment-age">(09 Jun '20, 19:20)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="75253"></span>
<div id="comment-75253" class="comment not_top_scorer">
<div id="post-75253-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also tried changing my baseURl in local.php from /nominatim to http://[my-ip]/nominatim/ but that didn't help either. Any other ideas?</p>
</div>
<div id="comment-75253-info" class="comment-info">
<span class="comment-age">(09 Jun '20, 19:29)</span> <span class="comment-user userinfo">bsilver</span>
</div>
</div>
<span id="75260"></span>
<div id="comment-75260" class="comment not_top_scorer">
<div id="post-75260-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can use <code>cd build; ./utils/query.php</code> to run test queries, which would show if the database imported fine (I'm sure it did). The <code>CONST_Website_BaseURL</code> in <code>local.php</code> is used to create links on the website, that's only relevant once the page is displayed. Check if system users (e.g. the user that starts the Apache webserver) can access the directory: <code>chmod a+x /srv/nominatim/</code> (<a href="http://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-20/#creating-dedicated-user-accounts)">http://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-20/#creating-dedicated-user-accounts)</a> Maybe you need to add <code>--recursive</code>.</p>
</div>
<div id="comment-75260-info" class="comment-info">
<span class="comment-age">(10 Jun '20, 01:56)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-75243" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-75243-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75305"></span>

<div id="answer-container-75305" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75305-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi <a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a>, due to a bug in the website I am unable to view your most recent comment with new troubleshooting suggestions. Are you able to view it and repost it as an answer?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '20, 14:25</strong></p>
<img src="https://secure.gravatar.com/avatar/3a3e3af440ad8ed5385f87e1957d1642?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bsilver&#39;s gravatar image" />
<p><span>bsilver</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bsilver has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75305" class="comments-container">
&#10;</div>
<div id="comment-tools-75305" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75305-form-container" class="comment-form-container">
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

