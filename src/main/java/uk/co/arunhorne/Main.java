package uk.co.arunhorne;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.concurrent.TimeUnit;

public class Main {

	private final static Logger log = LoggerFactory.getLogger(Main.class);

	public static void main(String[] args) throws InterruptedException {
		long counter = 0L;
		while (true) {
			log.info(counter++ + ": Once more unto the breach, dear friends, once more");
			Thread.sleep(TimeUnit.SECONDS.toMillis(1));
		}
	}

}

