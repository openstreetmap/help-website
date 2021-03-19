+++
type = "question"
title = "Pipe tcpdump from two machines to wireshark in my local machine"
description = '''Hi  My computer is running on windows 7. I need to do tcpdump on two different linux machines (machine2 and 3) that are only accessible from another linux machine (machine1) which is the only one I have access to, then pipe both of them results to my laptop to one instance of wireshark. Is this poss...'''
date = "2016-05-14T19:21:00Z"
lastmod = "2016-05-16T16:05:00Z"
weight = 52573
keywords = [ "pipe", "tcpdump", "wireshark" ]
aliases = [ "/questions/52573" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Pipe tcpdump from two machines to wireshark in my local machine](/questions/52573/pipe-tcpdump-from-two-machines-to-wireshark-in-my-local-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52573-score" class="post-score" title="current number of votes">0</div><span id="post-52573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi<br />
My computer is running on windows 7. I need to do tcpdump on two different linux machines (machine2 and 3) that are only accessible from another linux machine (machine1) which is the only one I have access to, then pipe both of them results to my laptop to one instance of wireshark. Is this possible to be done?. Or at least to only one machine? If this is possible could you please explain to me how can this be done, or any alternative. In summary<br />
</p><pre><code>client(windows-wireshark) -&gt; linux(machine1) -&gt; linux(machine2-tcpdump)    
                                             -&gt; linux(machine3-tcpdump)</code></pre><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pipe" rel="tag" title="see questions tagged &#39;pipe&#39;">pipe</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '16, 19:21</strong></p><img src="https://secure.gravatar.com/avatar/6ebdd129ea651d15f7888bf94b08d791?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carlos%20Lopez&#39;s gravatar image" /><p><span>Carlos Lopez</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carlos Lopez has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 May '16, 06:19</strong> </span></p></div></div><div id="comments-container-52573" class="comments-container"><span id="52586"></span><div id="comment-52586" class="comment"><div id="post-52586-score" class="comment-score"></div><div class="comment-text"><p>There are actually several things to deal with. If you need live captures, your main issue will be to make Wireshark capture from two pipes simultaneously. If you don't need live captures, it should be enough to save the capture output to files on the source machines, download the files, and merge them together on your Windows machine.</p><p>You may want to use the tunnelling capability of ssh to deliver the captured data from machines 2 and 3 to your Windows PC; if you have root rights at 2 and 3, you can make their local tcp port represent one at your PC, so whatever you send to localhost:X at machine2 will come to localhost:Y at your PC.</p><p>If you need more information, please specify more details about the whole arrangement.</p></div><div id="comment-52586-info" class="comment-info"><span class="comment-age">(15 May '16, 02:15)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="52591"></span><div id="comment-52591" class="comment"><div id="post-52591-score" class="comment-score"></div><div class="comment-text"><p>Sindy.<br />
Yes I need live captures of the two machines simultaneously (if possible) to be seen on my local machine on one instance of wireshark. I have root rights on machines 1, 2 and 3. Can you help me to set up the tunneling to achieve this?. I have used plink before to do this but only towards machine1, but now I need it towards 2,3 but the only access I have to reach 2 and 3 is through machine 1.<br />
Thanks.</p></div><div id="comment-52591-info" class="comment-info"><span class="comment-age">(15 May '16, 06:26)</span> <span class="comment-user userinfo">Carlos Lopez</span></div></div><span id="52593"></span><div id="comment-52593" class="comment"><div id="post-52593-score" class="comment-score"></div><div class="comment-text"><p>Do I get you right that you have already been using plink to capture remotely on a single linux machine and feed the output to Wireshark running on a Windows machine? So this part would be out of question? If so, were you also using a named pipe on Windows as part of that arrangement?</p></div><div id="comment-52593-info" class="comment-info"><span class="comment-age">(15 May '16, 07:08)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="52595"></span><div id="comment-52595" class="comment"><div id="post-52595-score" class="comment-score"></div><div class="comment-text"><p>That is correct.<br />
This is what I have in a .bat file<br />
</p><p>cd c:\<br />
</p><p>"Program Files (x86)/PuTTY/plink.exe" -ssh -pw root <span class="__cf_email__" data-cfemail="9eecf1f1eadeafaeb0afaeb0afaeb0af">[email protected]</span> "tcpdump -i eth1 -s 0 -U -n -w - 'tcp port not 22'" | "/wireshark/wireshark.exe" -k -i -<br />
</p><p>where 10.10.10.1 is machine 1<br />
</p><p>The previous .bat file opens wireshark and after a few seconds I can see the packets being captured. What I need is through machine1 do something similar towards 2 and 3.<br />
192.168.0.2 is machine2 192.168.0.3 is machine3 Thanks</p></div><div id="comment-52595-info" class="comment-info"><span class="comment-age">(15 May '16, 10:05)</span> <span class="comment-user userinfo">Carlos Lopez</span></div></div></div><div id="comment-tools-52573" class="comment-tools"></div><div class="clear"></div><div id="comment-52573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52599"></span>

<div id="answer-container-52599" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52599-score" class="post-score" title="current number of votes">0</div><span id="post-52599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Okay, so we have two points to address:</p><ul><li><p>how to make plink reach machine 2 (3) via machine 1,</p></li><li><p>how to make Wireshark capture from two queues simultaneously.</p></li></ul><p>The first one is easy: you use one instance of plink to log in to machine1 and set up a tunnel through that ssh session from your Windows machine's local tcp port to machine2's tcp port 22 the following way:</p><p><code>start "c:\Program Files (x86)\PuTTY\plink.exe" -ssh [email protected] -pw machine1_root_pwd -L 20022:machine2s_IP:22</code></p><p><code>machine2s_IP</code> is the IP address of machine2 which machine1 can access.</p><p>This will open a new command line window for that instance of plink but won't prevent the script from continuing further. You can get rid of that extra window by using a <code>/B</code> option to the <code>start</code> command but I'd recommend you to do that only after you debug the whole solution.</p><p>On the next line of the batch, you start the plink as you did, except that you specify the socket on your local machine as the server:</p><p><code>"c:\Program Files (x86)\PuTTY\plink.exe" -ssh [email protected] -P 20022 -pw mchn2_root_pwd "tcpdump -i eth1 -s 0 -U -n -w - 'tcp port not 22'" | wireshark ...</code></p><p>The second part is a bit of a headache. I've asked you on purpose whether you've already used a <strong>named</strong> pipe. The trouble is that you cannot feed Wireshark with two distinct streams through the (single) standard input (using <code>-i -</code>, you tell Wireshark to read the capture from standard input rather than a physical interface), so you'd have to use two distinct named pipes.</p><p>But while on linux it is possible to create and feed a named pipe from the command line, it seems not to be the case at Windows, so unless you'll find a ready-made solution, you'll need to write a piece of code in order to be able to set up the named pipes and feed them with the data output by the plink. So your command line options to Wireshark would be <code>-k -i \\.\pipe\from-machine-2 -i \\.\pipe\from-machine-3</code>, and you would have to start Wireshark with these options only as late as when both pipes have already come into existence. To make things more complex, the <code>-k</code> is necessary; if you omit it and then start the capture manually in the Wireshark window, it fails. Some suggestions can be found at the <a href="https://wiki.wireshark.org/CaptureSetup/Pipes">Wireshark wiki on pipes</a>. I use perl for the purpose, but I don't have a piece of code which would copy its standard input to the named queue and act as a buffer to temporarily store the input data as they arrive until Wireshark starts reading them.</p><p>So instead of using <code>|</code> to pipe plink's output straight to the standard input of Wireshark, you have to pipe it to that code:</p><p><code>start "c:\Program Files (x86)\PuTTY\plink.exe" -ssh [email protected] -P 20022 -pw mchn2_root_pwd "tcpdump -i eth1 -s 0 -U -n -w - 'tcp port not 22'" | your_pipe_writer from-machine-2</code></p><p><code>start "c:\Program Files (x86)\PuTTY\plink.exe" -ssh [email protected] -P 30022 -pw mchn3_root_pwd "tcpdump -i eth1 -s 0 -U -n -w - 'tcp port not 22'" | your_pipe_writer from-machine-3</code></p><p>And the last point is that despite what the Wiki says, Wireshark only accepts pcap (i.e. not pcapng) data format through stdin or named pipes, so depending on your tcpdump version, you may need to use the right option to make it output pcap. This excludes capturing on more than one interface by the same instance of tcpdump, i.e. in a generic case you'd need one tcpdump instance and named pipe per each source interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '16, 14:32</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 May '16, 21:55</strong> </span></p></div></div><div id="comments-container-52599" class="comments-container"><span id="52655"></span><div id="comment-52655" class="comment"><div id="post-52655-score" class="comment-score"></div><div class="comment-text"><p>Thanks Sindy, I will read your answer carefully, and will try to put it into practice. I may come back if you don't mind with another question related to this. Thanks.</p></div><div id="comment-52655-info" class="comment-info"><span class="comment-age">(16 May '16, 16:05)</span> <span class="comment-user userinfo">Carlos Lopez</span></div></div></div><div id="comment-tools-52599" class="comment-tools"></div><div class="clear"></div><div id="comment-52599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

