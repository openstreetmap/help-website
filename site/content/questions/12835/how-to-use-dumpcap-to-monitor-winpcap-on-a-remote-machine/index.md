+++
type = "question"
title = "how to use dumpcap to monitor winpcap on a remote machine"
description = '''I&#x27;ve been using wireshark to monitor a remote interface on a pc that is having an intermittent problem that we believe to be network related. The problem is, wireshark crashes on my win7 machine every 15 minutes or so after consuming more than a gig of RAM. I read that wireshark actually uses dumpca...'''
date = "2012-07-18T11:57:00Z"
lastmod = "2012-07-18T11:57:00Z"
weight = 12835
keywords = [ "winpcap", "remote", "dumpcap", "capture" ]
aliases = [ "/questions/12835" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to use dumpcap to monitor winpcap on a remote machine](/questions/12835/how-to-use-dumpcap-to-monitor-winpcap-on-a-remote-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12835-score" class="post-score" title="current number of votes">0</div><span id="post-12835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been using wireshark to monitor a remote interface on a pc that is having an intermittent problem that we believe to be network related. The problem is, wireshark crashes on my win7 machine every 15 minutes or so after consuming more than a gig of RAM.</p><p>I read that wireshark actually uses dumpcap to retrieve the packet info from winpcap. Unfortunately, to my knowledge, the documentation for dumpcap doesn't explain how to use dumpcap in this manner. So I viewed the dumpcap using ProcessThreadsView to see how wireshark was accomplishing this. What i found is that it was using several undocumented switches to get the info from the remote interface and then relay that back to wireshark.</p><p>Here are the steps I took to make this work.</p><ol><li>set up winpcap on the remote machine. Be sure to start the service once it is installed.</li><li>run wireshark on the local machine.</li><li>go to interfaces and add a remote interface pointing to the remote machine. I had to use an account that was local to the machine, NOT a domain account as winpcap seems to want to use the local machine to validate the credentials.</li><li>Note the device name/GUID for the remote interface and jot that down - you will need it later</li><li>Close wireshark!</li><li>From a command line, enter the following - of course swapping out the pertinent info for the IP of the remote machine, remote interface ID, username, and password</li></ol><p>"C:\Program Files\Wireshark\dumpcap" -n -i rpcap://[10.0.0.xxx]/\Device\NPF_<em>{8ED1D2B6-2FB7-41F7-A211-75D29414FFFF} -f "not tcp port 3389" -A username:password -w C:\Sniff\sniff_log</em></p><p>Note that in the documentation for dumpcap there is no mention of the -A switch to specify the UN/PW which will be necessary if your winpcap requires authorization. Happy sniffing!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span> <span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '12, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/a1a5e6f941533bc5634c4f0709f91880?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eyancey&#39;s gravatar image" /><p><span>eyancey</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eyancey has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Jul '12, 10:37</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-12835" class="comments-container"></div><div id="comment-tools-12835" class="comment-tools"></div><div class="clear"></div><div id="comment-12835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

