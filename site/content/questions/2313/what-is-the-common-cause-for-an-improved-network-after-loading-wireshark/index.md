+++
type = "question"
title = "What is the common cause for an improved network after loading Wireshark?"
description = '''Please help me understand the common cause between a loaded instance of Wireshark and improved network performance.  I had poor problems with the network in our house so after investigating the network I used Wireshark to peek around. The problem was most evident when I played an MMORPG Final Fantas...'''
date = "2011-02-13T14:07:00Z"
lastmod = "2011-02-13T16:20:00Z"
weight = 2313
keywords = [ "mmorpg", "network", "timeout", "wireshark" ]
aliases = [ "/questions/2313" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the common cause for an improved network after loading Wireshark?](/questions/2313/what-is-the-common-cause-for-an-improved-network-after-loading-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2313-score" class="post-score" title="current number of votes">0</div><span id="post-2313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Please help me understand the common cause between a loaded instance of Wireshark and improved network performance.<br />
</p><p>I had poor problems with the network in our house so after investigating the network I used Wireshark to peek around. The problem was most evident when I played an MMORPG Final Fantasy 14 but after loading it with an instance of Wireshark (and capturing data) in the background my load time dropped to 30 seconds from the usual 6+ minutes. Another PC in the had the same issues. After loading Wireshark the load times improved by the same magnitude.</p><p>The following day I loaded the game on the first PC without Wireshark and it took 6 minutes to load. After loading wireshark (without capturing data) the load time dropped to 30 seconds. The next day the load times were 30 seconds without having to load Wireshark.</p><p>The quality of our streaming video has greatly improved and web pages seem more responsive. There is a correlation that exists that I am unable to ignore. I understand that Wireshark doesn't do anything that would cause this. I only know enough about networks to put them together and get them to work, and do some simple troubleshooting.</p><p>About the home network: It's a home network in a fairly large house. We have a DLink DIR 655 bridged to a 2Wire 2701 HG-B, and are 30 meters apart. We had problems with online games, streaming video, and even had terrible load times with web pages and it wasn't unusual for the browser to return timeout messages.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mmorpg" rel="tag" title="see questions tagged &#39;mmorpg&#39;">mmorpg</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-timeout" rel="tag" title="see questions tagged &#39;timeout&#39;">timeout</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '11, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/e83ecddfd015878ce97786d772f092f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bugpop&#39;s gravatar image" /><p><span>Bugpop</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bugpop has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-2313" class="comments-container"></div><div id="comment-tools-2313" class="comment-tools"></div><div class="clear"></div><div id="comment-2313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2315"></span>

<div id="answer-container-2315" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2315-score" class="post-score" title="current number of votes">1</div><span id="post-2315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As you already said yourself, Wireshark doesn't do anything that would cause significantly better or worse load times. It is just a tool to observe what is happening on the network, not a tweaking or tuning tool. I guess the improved loading times are most certainly caused by the fact that the required data was already in the disk or memory caches, so the second time loading the game will be faster.</p><p>You could use Wireshark to determine the difference in network communication between the slow and fast tries, but for that you need to be good enough to tell what network packets are doing what. Especially in non-plain-text and/or undocumented protocols this is pretty difficult to do. Mostly you can try to determine how many connections were made while loading the game, how long they took from SYN to FIN/RST, and how much data was transfered. For that, the statistics tools can be off great help, especially the "Conversations" statistics. They will show you what communications where taking place and how long they took with which kind of data rate. Maybe you can spot a difference between fast and slow tries, but I still guess it's faster the 2nd time because of local caching.</p><p>Generally, trouble with Wireless over distances more than a few meters (and especially with walls in the way) is pretty common. The best option to get around those is to give the devices a clear line of sight and get them close together. If you can't do that, maybe a directional antenna with higher transmission power might help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '11, 16:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2315" class="comments-container"></div><div id="comment-tools-2315" class="comment-tools"></div><div class="clear"></div><div id="comment-2315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

