package com.data.collection.sample.data_collection;

import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;

import twitter4j.Paging;
import twitter4j.Query;
import twitter4j.QueryResult;
import twitter4j.Status;
import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;
import twitter4j.auth.Authorization;
import twitter4j.conf.ConfigurationBuilder;

public class Twitterr {

	public static Map<Long, TwitterDTO> tweets = new HashMap<Long, TwitterDTO>();
	public static List<List<String>> companies = new ArrayList<List<String>>();

	public static void main(String[] args) throws IOException {
		List<String> company = new ArrayList<String>();
		company.add("AdeccoWaytoWork");
		company.add("@AdeccoWaytoWork");
		companies.add(company);
		/*company = new ArrayList<String>();
		company.add("practicuscareer");
		company.add("@PracticusCareer");
		companies.add(company);
		company = new ArrayList<String>();
		company.add("practicusltd");
		company.add("@PracticusLtd");
		companies.add(company);*/
		Twitterr.getTweets();
	}

	public static void getTweets() {
		try {
			ConfigurationBuilder cb = new ConfigurationBuilder();
			cb.setDebugEnabled(true).setOAuthConsumerKey("37RxL0ssR8Rzznlcf6jkph9lB")
					.setOAuthConsumerSecret("iodDGgI15xp538Z4mvOdUlM0jyLZMKFhp8Df7DI5GOBW1vGljG")
					.setOAuthAccessToken("904044658484854785-C60ZPDdhwlL0fUNzoLlmXAr0K4EWD61")
					.setOAuthAccessTokenSecret("VzXGXpN8Elh14O4Asn98ZS8WWwIdMYLLClEQGsJ0dfgTG");
			System.setProperty("twitter4j.http.useSSL", "true");
			TwitterFactory tf = new TwitterFactory(cb.build());
			Twitter twitter = tf.getInstance();
			Authorization auth = twitter.getAuthorization();

			Paging paging = new Paging();
			paging.count(400);
			Long id = 0L;
			float score = 0f;
			HashSet<Long> uniqueTweetIDs = new HashSet<Long>();
			int size = 0;

			Writer writer = new BufferedWriter(new OutputStreamWriter(
					new FileOutputStream("C:\\Users\\tanumoy\\ITOrbital\\ITOrbital\\data-collection\\data.txt"),
					"utf-8"));

			for (List<String> compan : companies) {
				writer.write("============================== " + compan + " ==================================\r\n");
				System.out.println("============================== " + compan + " ==================================");
				for (String comp : compan) {
					paging = new Paging();
					paging.count(400);

					while (true) {
						List<Status> statuses = twitter.getUserTimeline(comp, paging);

						if (statuses.size() == 0)
							break;

						for (Status status : statuses) {
							id = status.getId();
							size = uniqueTweetIDs.size();
							uniqueTweetIDs.add(id);
							if (size < uniqueTweetIDs.size()) {
								TwitterDTO tweet = new TwitterDTO();
								if(status.isRetweet())
									tweet.setStatus(status.getRetweetedStatus().getText());
								else
									tweet.setStatus(status.getText());
								tweet.setRetweets(status.getRetweetCount());
								tweet.setLiked(status.getFavoriteCount());
								/*
								 * tweet.setComments(Twitterr.getDiscussion(
								 * status,twitter));
								 */
								tweet.setId(id);
								tweets.put(id, tweet);

								// writer.write("@" +
								// status.getUser().getScreenName() + " - " +
								// status.getText() + " ::: liked By::: " +
								// status.getFavoriteCount() + " ::: retwitted
								// By::: " + status.getRetweetCount()+"\r\n ");
								// System.out.println("@" +
								// status.getUser().getScreenName() + " - " +
								// status.getText() + " ::: liked By::: " +
								// status.getFavoriteCount() + " ::: retwitted
								// By::: " + status.getRetweetCount());
								score++;
								score = (float) (score + (status.getFavoriteCount() * 0.5));
								score = score + (status.getRetweetCount());
							}
						}
						paging.maxId(id - 1);
					}
				}
				writer.write("Final Count =============== " + score + " for " + compan.get(0) + "\r\n");
				System.out.println("Final Count =============== " + score + " for " + compan.get(0));
				Twitterr.getDiscussion(compan, twitter);
				Twitterr.printAndWrite(writer);
				score = 0;
				uniqueTweetIDs = new HashSet<Long>();

				tweets = new HashMap<Long, TwitterDTO>();
			}

			writer.close();
			/*
			 * Query query = new Query("practicus OR practicusltd");
			 * query.setCount(100); QueryResult result; do { result =
			 * twitter.search(query); List<Status> tweets = result.getTweets();
			 * for (Status tweet : tweets) { System.out.println("@" +
			 * tweet.getUser().getScreenName() + " - " + tweet.getText() +
			 * " ::: liked By::: " + tweet.getFavoriteCount() +
			 * " ::: retwitted By::: " + tweet.getRetweetCount()); } } while
			 * ((query = result.nextQuery()) != null);
			 */

			/*
			 * ResponseList<User> users = twitter.lookupUsers("practicusltd");
			 * for (User user : users) { if (user.getStatus() != null) {
			 * System.out.println("@" + user.getScreenName() + " - " +
			 * user.getStatus().getText()); } else { // the user is protected
			 * System.out.println("@" + user.getScreenName()); } }
			 */

			System.exit(0);
		} catch (TwitterException te) {
			te.printStackTrace();
			System.out.println("Failed to lookup users: " + te.getMessage());
			System.exit(-1);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public static void getDiscussion(List<String> screennames, Twitter twitter) {
		/*ArrayList<Status> replies = new ArrayList<Status>();

		ArrayList<Status> all = null;

		List<String> comments = new ArrayList<String>();*/

		for (String screenname : screennames) {
			try {
				Query query = new Query("to:" + screenname);

				System.out.println("query string: " + query.getQuery());

				/*
				 * try { query.setCount(100); } catch (Throwable e) { // enlarge
				 * buffer error? query.setCount(30); }
				 */

				QueryResult result = twitter.search(query);
				System.out.println("result: " + result.getTweets().size());

				//all = new ArrayList<Status>();

				do {
					System.out.println("do loop repetition");

					List<Status> tweets = result.getTweets();

					for (Status tweet : tweets){
						if (Twitterr.tweets.keySet().contains(tweet.getInReplyToStatusId())) {
							Twitterr.tweets.get(tweet.getInReplyToStatusId()).setComment(tweet.getId(), tweet.getText());
						}
					}
					/*if (all.size() > 0) {
						for (int i = all.size() - 1; i >= 0; i--)
							replies.add(all.get(i));
						all.clear();
					}
*/
					query = result.nextQuery();

					if (query != null)
						result = twitter.search(query);

				} while (query != null);

			} catch (Exception e) {
				e.printStackTrace();
			} catch (OutOfMemoryError e) {
				e.printStackTrace();
			}

		}
	}

	public static void printAndWrite(Writer writer) throws IOException{
		for(TwitterDTO tweet : Twitterr.tweets.values()){
			writer.write("TWEET ### "+tweet.getStatus()+"\n");
			System.out.println("TWEET ### "+tweet.getStatus());
			writer.write("##########Liked ## "+tweet.getLiked());
			System.out.println("##########Liked ## "+tweet.getLiked());
			writer.write("##########Shared ## "+tweet.getRetweets());
			System.out.println("##########Shared ## "+tweet.getRetweets());
			if(tweet.getComments().size()!=0){
				for(String comment:tweet.getComments()){
					writer.write("##########COMMENT ## "+comment+"\n");
					System.out.println("##########COMMENT ## "+comment);
				}
			}
		}
	}
}
