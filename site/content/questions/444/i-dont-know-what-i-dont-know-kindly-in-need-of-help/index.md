+++
type = "question"
title = "I don&#x27;t know what I don&#x27;t know. Kindly in need of help:"
description = '''I&#x27;ve been running a WAMPP (XP SP3) server over the years on the same static IP # in a non-commercial environment -- charities, family, non-profits, etc. -- using Joomla! CMS environs, even dating back to Mambo CMS days. Unfortunately I did not take the *nix route in the initial days of web server le...'''
date = "2010-10-06T13:20:00Z"
lastmod = "2010-10-07T01:43:00Z"
weight = 444
keywords = [ "non-unicasts", "dns" ]
aliases = [ "/questions/444" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [I don't know what I don't know. Kindly in need of help:](/questions/444/i-dont-know-what-i-dont-know-kindly-in-need-of-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-444-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-444-score" class="post-score" title="current number of votes">0</div><span id="post-444-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been running a WAMPP (XP SP3) server over the years on the same static IP # in a non-commercial environment -- charities, family, non-profits, etc. -- using Joomla! CMS environs, even dating back to Mambo CMS days. Unfortunately I did not take the *nix route in the initial days of web server learning experience which has been costly in terms of security and vulnerability. My typical security/attack response is an after-the-attack damage control as opposed to successful prevention. This is largely due to my ignorance.</p><p>In short, I'm experiencing 'oddities' once again and ran Wireshark (newbie user) to find several dns (53) and other connections that are concerning (non-unicasts, etc.) and kindly hope one can offer me some insight. I use Comodo Secure DNS servers and at boot found these:</p><pre><code>1   0.000000    192.168.2.103   156.154.70.22   DNS Standard query A 2o7.net
3   0.078757    192.168.2.103   156.154.70.22   DNS Standard query A hwcdn.net
5   0.121389    192.168.2.103   156.154.70.22   DNS Standard query A test.mockett.com
9   0.314756    192.168.2.103   156.154.70.22   DNS Standard query A host57.objectsciences.com (serveral objectsciences.com)
13  0.539002    192.168.2.103   156.154.70.22   DNS Standard query A RWTH-Aachen.DE
29  1.108054    192.168.2.103   156.154.70.22   DNS Standard query A nano2.dc.ukrtelecom.ua</code></pre>and so on...Please pardon me for I don't know what I don't know but these queries look alarming to me. Thank you in advance - SL</div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-non-unicasts" rel="tag" title="see questions tagged &#39;non-unicasts&#39;">non-unicasts</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '10, 13:20</strong></p><img src="https://secure.gravatar.com/avatar/35f99cae9c0c9545d7864640a82dc173?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sandl&#39;s gravatar image" /><p><span>Sandl</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sandl has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Oct '10, 13:51</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-444" class="comments-container"></div><div id="comment-tools-444" class="comment-tools"></div><div class="clear"></div><div id="comment-444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="454"></span>

<div id="answer-container-454" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-454-score" class="post-score" title="current number of votes">0</div><span id="post-454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Sandi...</p><p>The first step in determining if these truly are "oddities" is to identify the typical use of the domain names. For example, 2o7.net resolves for use by Adobe (see www.omniture.com/en/privacy/2o7?f=2o7). You can do some research on the domain names (or even do lookups by IP address using domaintools.com - I like this site and use it for traceback/reconnaissance work). hwcdn.net doesn't appear to be in use at the current time, however.</p><p>So... step 1 - is 156.154.70.22 the correct DNS server to go to? Step 2 - do some research on the domains to see if you can figure out why a client is looking for them. Step 3 - does your client connect/talk with the IP addresses offered in any DNS responses? Can you tell the purpose of that conversation (e.g., updating virus detection info).</p><p>I'll tell you that so many processes run automatically in the background that it often feel alarming when it's just normal "junk" - for example, I use Firefox with some plugins and when I launch my browser (not even looking at a site), the plugins connect to various sites to get updates. Messy, but harmless.</p><p>Regardless, better safe than sorry.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '10, 19:11</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-454" class="comments-container"><span id="456"></span><div id="comment-456" class="comment"><div id="post-456-score" class="comment-score"></div><div class="comment-text"><p>... or use dns lookup tools like Network-Tools.com: http://network-tools.com/</p></div><div id="comment-456-info" class="comment-info"><span class="comment-age">(07 Oct '10, 01:43)</span> <span class="comment-user userinfo">joke</span></div></div></div><div id="comment-tools-454" class="comment-tools"></div><div class="clear"></div><div id="comment-454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="455"></span>

<div id="answer-container-455" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-455-score" class="post-score" title="current number of votes">0</div><span id="post-455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please be aware that Wireshark itself does reverse lookups to show hostnames instead of IP addresses. For each packet it receives from a host it has not seen before, it will do a reverse lookup. So (many of) these DNS requests might have been there because you are running Wireshark.</p><p>You can disable name resolution in Wireshark under "View -&gt; Name Resolution", there you can deselect "Enable for Network Layer".</p><p>Does this lower the amount of DNS requests to a normal level?</p><p>If not, have a look at the configuration of your webserver logging. Webserver logging often also has the possibility of logging hostnames instead of IP addreses, so the source might be that too. In which case you need to find out how to dissable name resolving for your webserver.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '10, 23:51</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-455" class="comments-container"></div><div id="comment-tools-455" class="comment-tools"></div><div class="clear"></div><div id="comment-455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

