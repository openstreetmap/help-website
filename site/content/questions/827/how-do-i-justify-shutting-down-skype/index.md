+++
type = "question"
title = "How do I justify shutting down Skype?"
description = '''First off, Laura is great! Gerald is great! Wireshark is great! I&#x27;ve been digging into how Wireshark can help me detect security problems on my corporate network. I hear lots of talk about how bad Skype is and how nobody should allow it on their network. But I can&#x27;t seem to find anything that clearl...'''
date = "2010-11-05T12:46:00Z"
lastmod = "2011-02-13T07:27:00Z"
weight = 827
keywords = [ "security", "skype" ]
aliases = [ "/questions/827" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I justify shutting down Skype?](/questions/827/how-do-i-justify-shutting-down-skype)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-827-score" class="post-score" title="current number of votes">0</div><span id="post-827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>First off, Laura is great! Gerald is great! Wireshark is great!</p><p>I've been digging into how Wireshark can help me detect security problems on my corporate network. I hear lots of talk about how bad Skype is and how nobody should allow it on their network. But I can't seem to find anything that clearly shows <strong>why</strong> it is bad. How can I use Wireshark to plainly show why Skype should be banned from my network? I'm fighting an uphill battle because of the potential cost savings for employees traveling, especially internationally. Any help would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-security" rel="tag" title="see questions tagged &#39;security&#39;">security</span> <span class="post-tag tag-link-skype" rel="tag" title="see questions tagged &#39;skype&#39;">skype</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '10, 12:46</strong></p><img src="https://secure.gravatar.com/avatar/118ba0647042a5b2634b267f7291ed7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Network%20Dude&#39;s gravatar image" /><p><span>Network Dude</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Network Dude has no accepted answers">0%</span></p></div></div><div id="comments-container-827" class="comments-container"><span id="2297"></span><div id="comment-2297" class="comment"><div id="post-2297-score" class="comment-score"></div><div class="comment-text"><p>I can't speak to skype itself. But to me the answer would be to use some other VOIP protocol within your network. Use scype as a network transport outside your own network, convert at the DMZ, transport it via VPN to your phone room, unpackage it there, and inject into your PBX. Remember too that the phone system itself is a black box; that a lot of the switching box's hardware is not exactly bullet proof. And the cost of phone calls compared to the other costs of having an employee traveling is peanuts.</p></div><div id="comment-2297-info" class="comment-info"><span class="comment-age">(13 Feb '11, 07:27)</span> <span class="comment-user userinfo">SGBotsford</span></div></div></div><div id="comment-tools-827" class="comment-tools"></div><div class="clear"></div><div id="comment-827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="2160"></span>

<div id="answer-container-2160" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2160-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2160-score" class="post-score" title="current number of votes">2</div><span id="post-2160-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>http://blackhat.com/presentations/bh-europe-06/bh-eu-06-biondi/bh-eu-06-biondi-up.pdf</p><p>This one gives a more deep technical analysis of Skype, and is the base of why <em>I</em> don't trust Skype. To quote the summary:</p><ul><li>Good points<ul><li>Skype was made by clever people</li><li>Good use of cryptograph</li></ul></li><li><p>Bad points</p><ul><li>Hard to enforce a security policy with Skype</li><li>Jams traffic, can’t be distinguished from data exfiltration</li><li>Incompatible with traffic monitoring, IDS</li><li>Impossible to protect from attacks (which would be obfuscated)</li><li>Total blackbox. Lack of transparency.</li><li>No way to know if there is/will be a backdoor</li><li>Fully trusts anyone who speaks Skype.</li></ul></li></ul><p>And ask yourself: Can I really trust an application which does try so hard to limit me in figuring out what is going on? Can I trust an application which IDS's struggles to control? Can I trust a complete blackbox application, where it can't be verified that there are no security issues or a backdoor?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '11, 14:53</strong></p><img src="https://secure.gravatar.com/avatar/6eb7a9f90333d6d5f5182804909158f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dazo&#39;s gravatar image" /><p><span>dazo</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dazo has no accepted answers">0%</span></p></div></div><div id="comments-container-2160" class="comments-container"></div><div id="comment-tools-2160" class="comment-tools"></div><div class="clear"></div><div id="comment-2160-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="834"></span>

<div id="answer-container-834" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-834-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-834-score" class="post-score" title="current number of votes">0</div><span id="post-834-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A little googling:</p><ul><li><a href="http://blogs.technet.com/b/usefultechnology/archive/2006/06/27/438172.aspx">Why Skype is Bad</a></li><li>Skype: Big Bad Wolf? <a href="http://www.voipplanet.com/trends/article.php/3567391">part 1</a> / <a href="http://www.voipplanet.com/trends/article.php/3569171">part 2</a></li><li><a href="http://voxilla.com/2006/12/02/is-skype-bad-network-neighbor-102">Is Skype a Bad Network Neighbor?</a></li><li><a href="http://www.voip-news.com/feature/whats-wrong-with-skype-122707/">What's Wrong with Skype?</a></li></ul><p>Of course it is not all bad, Skype does work pretty well, you just have to decide for your company if the pros outweigh the cons and consider alternatives. Every company will have to do their own calculation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '10, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-834" class="comments-container"></div><div id="comment-tools-834" class="comment-tools"></div><div class="clear"></div><div id="comment-834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="843"></span>

<div id="answer-container-843" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-843-score" class="post-score" title="current number of votes">0</div><span id="post-843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Without reading those articles and just basing this on customer networks...</p><p>Many companies do not want Skype on their network because of bandwidth issues, use of personal time issues and security issues.</p><p>I use Skype as a business tool in my office, but I certainly wouldn't deploy it for everyone to use here. Like Sake said, it's a business decision. Have some fun and analyze some Skype traffic in a test environment!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '10, 19:50</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-843" class="comments-container"></div><div id="comment-tools-843" class="comment-tools"></div><div class="clear"></div><div id="comment-843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

